"""Tests for spawn_batch.py's naming-related logic: unique folder-name
reservation (including under real concurrency) and the startup scan that
finds which content hashes are already done.

This is deliberately the one part of spawn_batch.py worth testing directly:
it almost never matters in an ordinary run (two records rarely get the exact
same folder name; the scan almost always just sees clean, complete records)
but is exactly the part where a subtle bug — a race that lets two workers
claim the same name, a scan that misjudges a partial/failed record as done —
would silently corrupt output/ in whatever rare run does hit it, rather than
fail loudly.
"""
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from unittest.mock import MagicMock, patch

import utils
from spawn_batch import process_record, reserve_name, scan_existing_output


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


class TestReserveName:
    def test_first_claim_gets_the_base_name(self):
        names, lock = set(), threading.Lock()
        assert reserve_name("abc123-slug", names, lock) == "abc123-slug"

    def test_second_claim_of_same_base_gets_dash_2(self):
        names, lock = {"abc123-slug"}, threading.Lock()
        assert reserve_name("abc123-slug", names, lock) == "abc123-slug-2"

    def test_sequential_claims_increment(self):
        names, lock = set(), threading.Lock()
        results = [reserve_name("x", names, lock) for _ in range(5)]
        assert results == ["x", "x-2", "x-3", "x-4", "x-5"]

    def test_claimed_name_is_recorded_in_the_shared_set(self):
        names, lock = set(), threading.Lock()
        reserve_name("x", names, lock)
        assert "x" in names

    def test_unrelated_base_names_dont_collide(self):
        names, lock = set(), threading.Lock()
        assert reserve_name("a", names, lock) == "a"
        assert reserve_name("b", names, lock) == "b"

    def test_pre_existing_names_from_disk_are_respected(self):
        # Simulates a name already on disk from a previous run, not just one
        # claimed earlier in this process.
        names, lock = {"abc123-slug", "abc123-slug-2"}, threading.Lock()
        assert reserve_name("abc123-slug", names, lock) == "abc123-slug-3"

    def test_reserve_name_blocks_while_lock_is_held_externally(self):
        # The concurrent-claims tests below are a stress test, not proof: on
        # CPython, a bare check-then-add on a set is fast enough that the GIL
        # rarely preempts a thread mid-way, so an unlocked reserve_name can
        # pass those stress tests too (verified separately — 50 threads on a
        # barrier-synchronized start, 0 duplicates, with no lock at all). This
        # test instead proves reserve_name actually serializes on the lock it's
        # given: hold the lock externally, confirm a concurrent reserve_name
        # call blocks until it's released, rather than hoping to get lucky with
        # timing.
        names, lock = set(), threading.Lock()
        entered_critical_section = threading.Event()
        release_lock = threading.Event()

        def hold_lock_externally():
            with lock:
                entered_critical_section.set()
                release_lock.wait(timeout=2)

        holder = threading.Thread(target=hold_lock_externally)
        holder.start()
        assert entered_critical_section.wait(timeout=2)

        result = {}

        def call_reserve_name():
            result["name"] = reserve_name("x", names, lock)

        caller = threading.Thread(target=call_reserve_name)
        caller.start()
        caller.join(timeout=0.3)
        assert caller.is_alive()  # still blocked: reserve_name is waiting on the same lock

        release_lock.set()
        caller.join(timeout=2)
        assert not caller.is_alive()
        assert result["name"] == "x"
        holder.join()

    def test_concurrent_claims_of_the_same_base_are_all_unique(self):
        # A stress test, not a proof (see test_reserve_name_blocks_while_lock_is_held_externally
        # above for why): many ThreadPoolExecutor workers in spawn_batch.py
        # independently generating the same slug for genuinely different
        # records at the same moment. Still worth keeping — it exercises the
        # real code path under real thread contention and would catch a
        # regression that's slow enough, or unlucky enough, to actually race.
        names, lock = set(), threading.Lock()
        n = 50
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(lambda _: reserve_name("same-base", names, lock), range(n)))
        assert len(results) == n
        assert len(set(results)) == n  # every claimed name is unique

    def test_concurrent_claims_across_many_distinct_bases(self):
        # Same stress, but a realistic mix: mostly-distinct base names with a
        # handful of accidental repeats, matching what a real batch looks like.
        names, lock = set(), threading.Lock()
        bases = [f"base-{i % 10}" for i in range(200)]
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(lambda b: reserve_name(b, names, lock), bases))
        assert len(results) == len(set(results)) == 200


class TestProcessRecordNaming:
    """process_record is where the naming spec actually gets written to disk:
    the hash6-slug folder name, the full (untruncated) hash in metadata.json,
    and the harness/task/model/experiment/timestamp fields the skip-on-rerun
    scan and any future tooling depend on. docker itself is faked (see
    make_fake_docker_run) so these exercise the real folder-naming and
    metadata-writing code without needing a container.
    """

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
        # process startup (scan_existing_output, called once in main() before
        # any record is processed) — it has no way to see a same-hash record
        # that reaches process_record later in this same run, regardless of
        # whether that's a duplicate line in one batch file or two batch files
        # sharing content. Batch files are not a scoping boundary anywhere in
        # this system: dedup is always by full content hash against the
        # entire output dir. This test's names/lock stand in for that
        # in-process gap directly, without needing an actual duplicate line.
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

        done_hashes, names = scan_existing_output(out_dir)
        assert full_hash not in done_hashes
        assert orphan.name not in names

        _, name, ok, _ = self._run(tmp_path, full_hash=full_hash, names=names,
                                    names_lock=threading.Lock(), out_dir=out_dir)
        assert ok
        assert name == orphan.name  # reclaimed, not "-2"


class TestScanExistingOutput:
    def _write_metadata(self, folder: Path, **fields):
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "metadata.json").write_text(json.dumps(fields))

    def test_empty_directory(self, tmp_path):
        done, names = scan_existing_output(tmp_path)
        assert done == set()
        assert names == set()

    def test_missing_directory_does_not_crash(self, tmp_path):
        done, names = scan_existing_output(tmp_path / "does-not-exist")
        assert done == set()
        assert names == set()

    def test_successful_record_is_marked_done(self, tmp_path):
        self._write_metadata(tmp_path / "abc123-some-slug", hash="fullhash1",
                              timestamp="2026-01-01T00:00:00+00:00")
        done, names = scan_existing_output(tmp_path)
        assert done == {"fullhash1"}
        assert "abc123-some-slug" in names

    def test_failed_record_not_marked_done_but_its_name_is_still_reserved(self, tmp_path):
        folder = tmp_path / "abc123-some-slug"
        folder.mkdir(parents=True)
        (folder / "stdout.log").write_text("")
        (folder / "stderr.log").write_text("boom")
        done, names = scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_partial_metadata_missing_timestamp_not_marked_done(self, tmp_path):
        # Written-but-not-yet-completed shape shouldn't count as done, in
        # case a future version starts writing metadata.json earlier.
        self._write_metadata(tmp_path / "abc123-some-slug", hash="fullhash1")
        done, names = scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_corrupt_metadata_json_does_not_crash_the_scan(self, tmp_path):
        folder = tmp_path / "abc123-some-slug"
        folder.mkdir(parents=True)
        (folder / "metadata.json").write_text("{not valid json")
        done, names = scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_unrelated_top_level_file_is_ignored(self, tmp_path):
        (tmp_path / "some-stray-file.txt").write_text("hi")
        done, names = scan_existing_output(tmp_path)
        assert names == set()

    def test_multiple_records_of_mixed_status_all_collected_correctly(self, tmp_path):
        self._write_metadata(tmp_path / "aaa-one", hash="h1", timestamp="t")
        self._write_metadata(tmp_path / "bbb-two", hash="h2", timestamp="t")
        failed = tmp_path / "ccc-three"
        failed.mkdir()
        (failed / "stderr.log").write_text("failed")
        done, names = scan_existing_output(tmp_path)
        assert done == {"h1", "h2"}
        assert names == {"aaa-one", "bbb-two", "ccc-three"}
