"""Tests for spawn_batch.py's process_record: where the naming spec actually
gets written to disk (the hash6-slug folder name, the full untruncated hash in
metadata.json, and the harness/task/model/experiment/timestamp fields the
skip-on-rerun scan and any future tooling depend on). docker itself is faked
(see make_fake_docker_run) so these exercise the real folder-naming and
metadata-writing code without needing a container.

reserve_name and scan_existing_output themselves now live in utils.py — see
test_utils.py for their tests.
"""
import json
import threading
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

import utils
from spawn_batch import process_record


def make_fake_docker_run(produce_files=True, returncode=0):
    """A stand-in for subprocess.run(["docker", "run", ...]): writes a fake
    harness output file into whatever scratch dir process_record mounted at
    /output (found by scanning the real docker cmd for its "-v host:/output"
    arg), so process_record's real copy-into-dest and metadata-writing code
    runs against something, without needing a real container.
    """
    def fake_run(cmd, capture_output=True, text=True):
        mount = next(a for a in cmd if a.endswith(":/output"))
        scratch = Path(mount[: -len(":/output")])
        if produce_files:
            (scratch / "translation.bc").write_text("<|program|> pass")
        result = MagicMock()
        result.returncode = returncode
        result.stdout = "fake stdout"
        result.stderr = "fake stderr"
        return result
    return fake_run


class TestProcessRecordNaming:
    def _run(self, tmp_path, record_line="{}", full_hash="a" * 64,
             harness_name="opencode", task_name="discovery",
             model="vertex-proxy/gemini-flash", experiment=None,
             produce_files=True, returncode=0, names=None, names_lock=None,
             out_dir=None):
        names = set() if names is None else names
        names_lock = names_lock or threading.Lock()
        design_doc = tmp_path / "DESIGN_DOC.md"
        design_doc.write_text("design")
        prompt_file = tmp_path / "prompt.md"
        prompt_file.write_text("prompt")
        if out_dir is None:
            out_dir = tmp_path / "output"
        out_dir.mkdir(exist_ok=True)

        with patch("spawn_batch.utils.generate_slug", return_value="fixed-slug"), \
             patch("spawn_batch.subprocess.run", side_effect=make_fake_docker_run(produce_files, returncode)):
            name, ok, tail = process_record(
                record_line, full_hash, "fake-image", design_doc, prompt_file,
                model, "key", "http://base", harness_name, task_name, experiment,
                out_dir, names, names_lock,
            )
        return out_dir, name, ok, tail

    def test_folder_name_is_hash6_and_slug(self, tmp_path):
        out_dir, name, ok, _ = self._run(tmp_path, full_hash="abcdef" + "0" * 58)
        assert ok
        assert name == "abcdef-fixed-slug"

    def test_metadata_stores_full_hash_not_truncated(self, tmp_path):
        full_hash = "abcdef" + "0" * 58
        out_dir, name, _, _ = self._run(tmp_path, full_hash=full_hash)
        meta = json.loads((out_dir / name / "metadata.json").read_text())
        assert meta["hash"] == full_hash
        assert len(meta["hash"]) == 64

    def test_metadata_contains_harness_task_model(self, tmp_path):
        out_dir, name, _, _ = self._run(tmp_path, harness_name="pi", task_name="discovery",
                                         model="vertex-proxy/gemini-flash")
        meta = json.loads((out_dir / name / "metadata.json").read_text())
        assert meta["harness"] == "pi"
        assert meta["task"] == "discovery"
        assert meta["model"] == "vertex-proxy/gemini-flash"

    def test_metadata_timestamp_is_present_and_parseable(self, tmp_path):
        out_dir, name, _, _ = self._run(tmp_path)
        meta = json.loads((out_dir / name / "metadata.json").read_text())
        datetime.fromisoformat(meta["timestamp"])  # raises if malformed

    def test_metadata_experiment_defaults_to_none(self, tmp_path):
        out_dir, name, _, _ = self._run(tmp_path, experiment=None)
        meta = json.loads((out_dir / name / "metadata.json").read_text())
        assert meta["experiment"] is None

    def test_metadata_experiment_recorded_when_given(self, tmp_path):
        out_dir, name, _, _ = self._run(tmp_path, experiment="mined-batch-3")
        meta = json.loads((out_dir / name / "metadata.json").read_text())
        assert meta["experiment"] == "mined-batch-3"

    def test_source_json_preserves_original_record_line(self, tmp_path):
        out_dir, name, _, _ = self._run(tmp_path, record_line='{"foo": "bar"}')
        assert (out_dir / name / "source.json").read_text() == '{"foo": "bar"}'

    def test_no_metadata_when_harness_produces_nothing(self, tmp_path):
        # returncode 0 ("success") but nothing landed in /output — must not be
        # mistaken for done, or a rerun would wrongly skip this record forever.
        out_dir, name, ok, tail = self._run(tmp_path, produce_files=False, returncode=0)
        assert ok is False
        assert not (out_dir / name / "metadata.json").exists()
        assert (out_dir / name / "stderr.log").exists()

    def test_no_metadata_when_harness_exits_nonzero_even_if_files_produced(self, tmp_path):
        out_dir, name, ok, tail = self._run(tmp_path, produce_files=True, returncode=1)
        assert ok is False
        assert not (out_dir / name / "metadata.json").exists()

    def test_two_records_with_the_same_hash_in_one_process_get_suffixed_names(self, tmp_path):
        # Dedup against already-done work is a one-time snapshot taken at
        # process startup (utils.scan_existing_output, called once in main()
        # before any record is processed) — it has no way to see a same-hash
        # record that reaches process_record later in this same run, regardless
        # of whether that's a duplicate line in one batch file or two batch
        # files sharing content. Batch files are not a scoping boundary
        # anywhere in this system: dedup is always by full content hash
        # against the entire output dir. This test's names/lock stand in for
        # that in-process gap directly, without needing an actual duplicate line.
        names, lock = set(), threading.Lock()
        full_hash = "abcdef" + "0" * 58
        out_dir = tmp_path / "output"
        _, name1, ok1, _ = self._run(tmp_path, full_hash=full_hash, names=names,
                                      names_lock=lock, out_dir=out_dir)
        _, name2, ok2, _ = self._run(tmp_path, full_hash=full_hash, names=names,
                                      names_lock=lock, out_dir=out_dir)
        assert ok1 and ok2
        assert name2 == name1 + "-2"
        assert (out_dir / name1 / "metadata.json").exists()
        assert (out_dir / name2 / "metadata.json").exists()

    def test_retry_after_pruning_a_crash_orphan_reclaims_the_original_name(self, tmp_path):
        # A crash mid-run leaves a folder with only source.json — no
        # metadata.json, no logs. Simulate that, then a fresh process
        # starting up: prune_incomplete_folders should remove it before
        # scan_existing_output runs, so the retry's reserve_name never sees
        # the orphan's name as taken and gets the original name back instead
        # of a `-2`.
        out_dir = tmp_path / "output"
        out_dir.mkdir()
        full_hash = "abcdef" + "0" * 58
        orphan = out_dir / utils.build_folder_name(full_hash, "fixed-slug")
        orphan.mkdir()
        (orphan / "source.json").write_text("{}")

        removed = utils.prune_incomplete_folders(out_dir)
        assert removed == [orphan.name]

        done_hashes, names = utils.scan_existing_output(out_dir)
        assert full_hash not in done_hashes
        assert orphan.name not in names

        _, name, ok, _ = self._run(tmp_path, full_hash=full_hash, names=names,
                                    names_lock=threading.Lock(), out_dir=out_dir)
        assert ok
        assert name == orphan.name  # reclaimed, not "-2"
