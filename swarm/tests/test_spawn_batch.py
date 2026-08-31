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
import subprocess
import threading
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

import spawn_batch
import utils
from spawn_batch import process_record


def make_fake_docker_run(produce_files=True, returncode=0, stderr="fake stderr"):
    """A stand-in for subprocess.run(["docker", "run", ...]): writes a fake
    harness output file into whatever scratch dir process_record mounted at
    /output (found by scanning the real docker cmd for its "-v host:/output"
    arg), so process_record's real copy-into-dest and metadata-writing code
    runs against something, without needing a real container.
    """
    def fake_run(cmd, capture_output=True, text=True, timeout=None):
        mount = next(a for a in cmd if a.endswith(":/output"))
        scratch = Path(mount[: -len(":/output")])
        if produce_files:
            (scratch / "translation.bc").write_text("<|program|> pass")
        result = MagicMock()
        result.returncode = returncode
        result.stdout = "fake stdout"
        result.stderr = stderr
        return result
    return fake_run


class TestProcessRecordNaming:
    def _run(self, tmp_path, record_line="{}", full_hash="a" * 64,
             harness_name="opencode", task_name="discovery",
             model="vertex-proxy/gemini-flash", experiment=None,
             produce_files=True, returncode=0, names=None, names_lock=None,
             out_dir=None, stderr="fake stderr", timeout_s=1200):
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
             patch("spawn_batch.subprocess.run", side_effect=make_fake_docker_run(produce_files, returncode, stderr)):
            name, ok, tail = process_record(
                record_line, full_hash, "fake-image", design_doc, prompt_file,
                model, "key", "http://base", harness_name, task_name, experiment,
                timeout_s, out_dir, names, names_lock,
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

    def _run_timing_out(self, tmp_path, timeout_s=5, full_hash="abcdef" + "0" * 58):
        """process_record against a docker run that never returns."""
        killed = []

        def fake_run(cmd, capture_output=True, text=True, timeout=None):
            if cmd[:2] == ["docker", "kill"]:
                killed.append(cmd[2])
                return MagicMock(returncode=0, stdout="", stderr="")
            raise subprocess.TimeoutExpired(cmd, timeout, output=b"partial out",
                                            stderr=b"partial err")

        names, lock = set(), threading.Lock()
        design_doc = tmp_path / "DESIGN_DOC.md"; design_doc.write_text("d")
        prompt_file = tmp_path / "prompt.md"; prompt_file.write_text("p")
        out_dir = tmp_path / "output"; out_dir.mkdir(exist_ok=True)
        with patch("spawn_batch.utils.generate_slug", return_value="fixed-slug"), \
             patch("spawn_batch.subprocess.run", side_effect=fake_run):
            name, ok, tail = process_record(
                "{}", full_hash, "img", design_doc, prompt_file, "m", "k", "b",
                "opencode", "discovery", None, timeout_s, out_dir, names, lock)
        return out_dir, name, ok, tail, killed

    def test_a_hung_container_is_killed_by_name_not_just_detached(self, tmp_path):
        # subprocess's own timeout only kills the `docker run` client; the
        # container keeps running and keeps its CPU. Killing it needs the name,
        # which is why build_docker_cmd takes one.
        out_dir, name, ok, tail, killed = self._run_timing_out(tmp_path)
        assert ok is False
        assert killed == [f"swarm-{name}"]

    def test_timeout_is_recorded_as_a_distinct_returncode_with_an_explanation(self, tmp_path):
        # Harnesses buffer output, so a killed container's transcript is often
        # empty; without the appended note failure.json would carry a bare exit
        # code and nothing saying the record was killed rather than crashed.
        out_dir, _, _, tail, _ = self._run_timing_out(tmp_path, timeout_s=7)
        meta = json.loads((out_dir.parent / "failures" / "abcdef" / "failure.json").read_text())
        assert meta["returncode"] == spawn_batch.TIMEOUT_RETURNCODE
        assert "timed out after 7s" in (out_dir.parent / "failures" / "abcdef" / "stderr.log").read_text()
        # The timeout must win over anything the harness said earlier — that is
        # why it is written last, in the `Error:` convention.
        assert meta["error"] == "timed out after 7s and was killed."
        assert "timed out after 7s" in tail

    def test_whatever_was_captured_before_the_kill_is_kept(self, tmp_path):
        out_dir, _, _, _, _ = self._run_timing_out(tmp_path)
        d = out_dir.parent / "failures" / "abcdef"
        assert "partial out" in (d / "stdout.log").read_text()
        assert "partial err" in (d / "stderr.log").read_text()

    def test_failure_logs_go_to_failures_dir_and_out_dir_folder_is_removed(self, tmp_path):
        # out_dir is for successes; a failed attempt's logs live under
        # failures/ instead, so nothing has to be rescued by hand before the
        # next run prunes out_dir.
        out_dir, name, ok, _ = self._run(tmp_path, produce_files=False,
                                         full_hash="abcdef" + "0" * 58)
        assert ok is False
        assert not (out_dir / name).exists()
        failure = out_dir.parent / "failures" / "abcdef"
        assert (failure / "stderr.log").read_text() == "fake stderr"
        assert (failure / "stdout.log").read_text() == "fake stdout"
        assert (failure / "source.json").exists()

    def test_failure_json_records_exit_code_and_that_nothing_was_produced(self, tmp_path):
        # The silent-stall shape: exits 0, writes nothing, reports no error.
        # Without the exit code recorded, that is indistinguishable after the
        # fact from a container that was killed.
        # Silent means the harness said nothing at all — hence stderr="".
        # A harness that reports an HTTP failure clearly (pi's "503 status
        # code") must not land in this bucket, so error is only None here.
        out_dir, _, _, _ = self._run(tmp_path, produce_files=False, returncode=0,
                                     full_hash="abcdef" + "0" * 58, stderr="")
        meta = json.loads((out_dir.parent / "failures" / "abcdef" / "failure.json").read_text())
        assert meta["returncode"] == 0
        assert meta["produced_files"] is False
        assert meta["error"] is None  # nothing reported — the silent signature
        assert meta["hash"] == "abcdef" + "0" * 58
        assert isinstance(meta["duration_s"], float)
        datetime.fromisoformat(meta["timestamp"])  # raises if malformed

    def test_partial_output_is_preserved_when_the_harness_wrote_files_then_failed(self, tmp_path):
        # The near-miss case: files written, then a non-zero exit (e.g. a 429
        # on the last step). Still a failure — the task's contract is all four
        # files, so no metadata.json and a rerun retries it — but the work it
        # did manage is kept under partial/ instead of being deleted.
        out_dir, name, ok, tail = self._run(tmp_path, produce_files=True, returncode=1,
                                            full_hash="abcdef" + "0" * 58)
        assert ok is False
        assert not (out_dir / name).exists()
        failure = out_dir.parent / "failures" / "abcdef"
        assert (failure / "partial" / "translation.bc").read_text() == "<|program|> pass"
        meta = json.loads((failure / "failure.json").read_text())
        assert meta["produced_files"] is True
        assert meta["partial_files"] == ["translation.bc"]
        assert "partial output kept" in tail

    def test_no_partial_dir_when_the_harness_wrote_nothing(self, tmp_path):
        out_dir, _, _, tail = self._run(tmp_path, produce_files=False, returncode=0,
                                        full_hash="abcdef" + "0" * 58)
        failure = out_dir.parent / "failures" / "abcdef"
        assert not (failure / "partial").exists()
        meta = json.loads((failure / "failure.json").read_text())
        assert meta["partial_files"] == []
        assert "partial output kept" not in tail

    def test_a_reported_http_failure_is_not_classified_as_silent(self, tmp_path):
        # pi's wording. Before last_error_line handled it, 96 of these were
        # reported as "no error reported", indistinguishable from a container
        # that produced nothing and complained about nothing.
        out_dir, _, _, tail = self._run(tmp_path, produce_files=False, returncode=1,
                                        full_hash="abcdef" + "0" * 58,
                                        stderr="503 status code (no body)")
        meta = json.loads((out_dir.parent / "failures" / "abcdef" / "failure.json").read_text())
        assert meta["error"] == "HTTP 503"
        assert "no error reported" not in tail

    def test_same_record_failing_twice_gets_one_directory_per_attempt(self, tmp_path):
        # First of the two reasons a name gets suffixed: the same record
        # failing again, which is the common case since a re-run retries
        # exactly what failed. Each attempt keeps its own logs.
        out_dir = tmp_path / "output"
        full_hash = "abcdef" + "0" * 58
        for _ in range(3):
            self._run(tmp_path, produce_files=False, full_hash=full_hash, out_dir=out_dir)
        failures = out_dir.parent / "failures"
        assert sorted(p.name for p in failures.iterdir()) == ["abcdef", "abcdef-2", "abcdef-3"]
        # The full hash, not the name, is what groups attempts by record.
        hashes = {json.loads((d / "failure.json").read_text())["hash"]
                  for d in failures.iterdir()}
        assert hashes == {full_hash}

    def test_two_records_sharing_a_hash6_prefix_do_not_overwrite_each_other(self, tmp_path):
        # The other reason: distinct records whose hashes share the first 6 hex
        # chars — rare per pair, near-certain across a corpus this size. Their
        # logs must stay separate, and the recorded full hash is what tells
        # them apart despite the near-identical names.
        out_dir = tmp_path / "output"
        a = "abcdef" + "0" * 58
        b = "abcdef" + "1" * 58
        self._run(tmp_path, produce_files=False, full_hash=a, out_dir=out_dir,
                  record_line='{"which": "a"}')
        self._run(tmp_path, produce_files=False, full_hash=b, out_dir=out_dir,
                  record_line='{"which": "b"}')
        failures = out_dir.parent / "failures"
        assert sorted(p.name for p in failures.iterdir()) == ["abcdef", "abcdef-2"]
        by_hash = {json.loads((d / "failure.json").read_text())["hash"]:
                   (d / "source.json").read_text() for d in failures.iterdir()}
        assert by_hash == {a: '{"which": "a"}', b: '{"which": "b"}'}

    def test_success_leaves_an_earlier_failure_in_place(self, tmp_path):
        # failures/ is attempt history, not a to-do list: whether a record
        # eventually succeeded is answered by out_dir, so a later success does
        # not erase the record of what went wrong before it.
        out_dir = tmp_path / "output"
        full_hash = "abcdef" + "0" * 58
        self._run(tmp_path, produce_files=False, full_hash=full_hash, out_dir=out_dir)
        self._run(tmp_path, produce_files=True, full_hash=full_hash, out_dir=out_dir)
        assert (out_dir.parent / "failures" / "abcdef" / "failure.json").exists()

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
