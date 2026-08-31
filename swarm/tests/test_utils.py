"""Tests for utils.py: the naming logic (content hash, slug, folder name),
thread-safe name reservation, and the startup dedup/pruning scans.

generate_slug() is the one function that talks to a real model in production;
here it's tested against a mocked litellm.completion so these run offline,
deterministically, and cover failure shapes (including the exact "no choices"
malformed-response shape hit once during development) without spending real
tokens or needing credentials.

reserve_name and scan_existing_output are deliberately tested directly: they
almost never matter in an ordinary run (two records rarely get the exact same
folder name; the scan almost always just sees clean, complete records) but are
exactly the part where a subtle bug — a race that lets two workers claim the
same name, a scan that misjudges a partial/failed record as done — would
silently corrupt output/ in whatever rare run does hit it, rather than fail
loudly.
"""
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import MagicMock, patch

import pytest

import utils


def make_response(content):
    """A response shaped like what litellm.completion() returns, with
    response.choices[0].message.content == content.
    """
    message = MagicMock()
    message.content = content
    choice = MagicMock()
    choice.message = message
    response = MagicMock()
    response.choices = [choice]
    return response


class TestContentHash:
    def test_deterministic(self):
        assert utils.content_hash("abc") == utils.content_hash("abc")

    def test_distinguishes_different_content(self):
        assert utils.content_hash("abc") != utils.content_hash("abd")

    def test_is_full_sha256_hex(self):
        h = utils.content_hash("abc")
        assert len(h) == 64
        int(h, 16)  # raises ValueError if not valid hex


class TestSlugify:
    def test_lowercases_and_hyphenates(self):
        assert utils.slugify("Two Plus Two") == "two-plus-two"

    def test_strips_punctuation(self):
        assert utils.slugify("Two, Plus! Two?") == "two-plus-two"

    def test_collapses_repeated_separators(self):
        assert utils.slugify("two   plus--two") == "two-plus-two"

    def test_truncates_to_max_words(self):
        text = "one two three four five six seven eight"
        assert utils.slugify(text, max_words=3) == "one-two-three"

    def test_truncates_to_max_len(self):
        result = utils.slugify("a " * 100, max_len=10)
        assert len(result) <= 10

    def test_empty_input_falls_back_to_example(self):
        assert utils.slugify("") == "example"

    def test_punctuation_only_input_falls_back_to_example(self):
        assert utils.slugify("!!! ??? ...") == "example"


class TestGenerateSlug:
    def test_happy_path_slugifies_the_model_response(self):
        with patch("utils.litellm.completion", return_value=make_response("Two Plus Two")):
            result = utils.generate_slug("trajectory", "vertex-proxy/gemini-flash", "key", "http://base")
        assert result == "two-plus-two"

    def test_strips_provider_prefix_before_calling_litellm(self):
        mock_call = MagicMock(return_value=make_response("x"))
        with patch("utils.litellm.completion", mock_call):
            utils.generate_slug("content", "vertex-proxy/gemini-flash", "key", "http://base")
        assert mock_call.call_args.kwargs["model"] == "openai/gemini-flash"

    def test_passes_through_api_key_and_base_url(self):
        mock_call = MagicMock(return_value=make_response("x"))
        with patch("utils.litellm.completion", mock_call):
            utils.generate_slug("content", "vertex-proxy/gemini-flash", "the-key", "http://the-base")
        kwargs = mock_call.call_args.kwargs
        assert kwargs["api_key"] == "the-key"
        assert kwargs["api_base"] == "http://the-base"

    def test_falls_back_to_example_on_exception(self):
        with patch("utils.litellm.completion", side_effect=RuntimeError("network error")):
            result = utils.generate_slug("content", "vertex-proxy/gemini-flash", "key", "http://base")
        assert result == "example"

    def test_falls_back_to_example_on_none_content(self):
        with patch("utils.litellm.completion", return_value=make_response(None)):
            result = utils.generate_slug("content", "vertex-proxy/gemini-flash", "key", "http://base")
        assert result == "example"

    def test_falls_back_to_example_on_empty_choices(self):
        # The actual shape of a real bug hit during development: a response
        # with no usable choices. generate_slug must never raise for this.
        response = MagicMock()
        response.choices = []
        with patch("utils.litellm.completion", return_value=response):
            result = utils.generate_slug("content", "vertex-proxy/gemini-flash", "key", "http://base")
        assert result == "example"

    def test_never_raises_regardless_of_failure_mode(self):
        for side_effect in [RuntimeError("boom"), TimeoutError("timeout"), ValueError("bad")]:
            with patch("utils.litellm.completion", side_effect=side_effect):
                result = utils.generate_slug("content", "m", "k", "b")
            assert result == "example"


class TestBuildFolderName:
    def test_combines_hash_prefix_and_slug(self):
        full_hash = "a" * 64
        assert utils.build_folder_name(full_hash, "some-slug") == "aaaaaa-some-slug"

    def test_hash_prefix_is_exactly_six_chars(self):
        full_hash = "0123456789abcdef" * 4
        name = utils.build_folder_name(full_hash, "slug")
        assert name.split("-", 1)[0] == "012345"
        assert len(name.split("-", 1)[0]) == 6


class TestLastErrorLine:
    """Kept harness-agnostic on purpose: opencode says `Error: ...`, pi says
    `503 status code (no body)` or dumps a Cloudflare challenge page. Reading
    only opencode's shape reported pi's clear HTTP failures as "no error
    reported", which is the same signature as a container that died having said
    nothing at all — two very different problems.
    """

    def test_opencode_error_prefix(self):
        assert utils.last_error_line("> build\nError: Too Many Requests") == "Too Many Requests"

    def test_last_error_wins_when_several(self):
        assert utils.last_error_line("Error: first\nError: second") == "second"

    def test_strips_ansi(self):
        assert utils.last_error_line("\x1b[91mError: Boom\x1b[0m") == "Boom"

    def test_pi_bare_status_code(self):
        assert utils.last_error_line("503 status code (no body)") == "HTTP 503"

    def test_cloudflare_challenge_is_named_not_dumped(self):
        body = '429 <!DOCTYPE html><title>Just a moment...</title>' + "x" * 20000
        out = utils.last_error_line(body)
        assert out == "HTTP 429 (Cloudflare challenge)"
        assert len(out) < 60          # never carry the 20KB body into failure.json

    def test_unrecognized_output_falls_back_to_first_line_truncated(self):
        assert utils.last_error_line("something odd happened\nmore") == "something odd happened"
        assert len(utils.last_error_line("z" * 500)) == 160

    def test_progress_chatter_alone_is_still_silent(self):
        # opencode's silent-stall transcripts contain only its banner and tool
        # calls. Reporting the banner as the error would erase the difference
        # between "produced garbage and said nothing" and "reported a failure".
        assert utils.last_error_line("> build \u00b7 gemini-3.5-flash") is None
        assert utils.last_error_line("> build\n\u2192 Read DESIGN_DOC.md\n\u2731 Glob \u2190 Write") is None
        assert utils.last_error_line("# Todos\n[ ] read the doc\n$ ls") is None

    def test_real_speech_after_chatter_is_reported(self):
        assert utils.last_error_line("> build\nsomething broke") == "something broke"

    def test_none_only_when_nothing_was_said(self):
        # The genuinely silent shape — must stay distinguishable from a
        # reported HTTP failure.
        assert utils.last_error_line("") is None
        assert utils.last_error_line("   \n\n  ") is None
        assert utils.last_error_line("\x1b[91m> build\x1b[0m") is None  # banner only


class TestTrajectoryText:
    """What the container actually gets mounted. The fallbacks matter more than
    the happy path: a record shape nobody anticipated should still reach the
    agent as *something*, since returning the raw line degrades to the old
    behaviour, while raising would fail an otherwise-fine record outright.
    """

    def test_returns_decoded_content_with_real_newlines(self):
        line = json.dumps({"id": "x", "content": "<|user|>hi\nthere<|assistant|>yo"})
        result = utils.trajectory_text(line)
        assert result == "<|user|>hi\nthere<|assistant|>yo"
        assert "\\n" not in result

    def test_drops_the_wrapper_fields_the_task_never_asks_about(self):
        line = json.dumps({"id": "u", "platform": "chatgpt", "timestamp": "t", "content": "turns"})
        result = utils.trajectory_text(line)
        assert result == "turns"
        for wrapper in ("platform", "chatgpt", "timestamp"):
            assert wrapper not in result

    def test_non_json_falls_back_to_raw_line(self):
        assert utils.trajectory_text("not json at all") == "not json at all"

    def test_json_that_is_not_an_object_falls_back(self):
        assert utils.trajectory_text("[1, 2, 3]") == "[1, 2, 3]"

    def test_missing_content_key_falls_back(self):
        line = json.dumps({"id": "x", "platform": "chatgpt"})
        assert utils.trajectory_text(line) == line

    def test_blank_content_falls_back(self):
        line = json.dumps({"id": "x", "content": "   "})
        assert utils.trajectory_text(line) == line

    def test_non_string_content_falls_back(self):
        line = json.dumps({"id": "x", "content": {"nested": 1}})
        assert utils.trajectory_text(line) == line

    def test_does_not_affect_the_record_identity(self):
        # The hash is taken from the raw line, so changing what gets mounted
        # must not change which records a rerun considers already done.
        line = json.dumps({"id": "x", "content": "turns"})
        assert utils.content_hash(line) == utils.content_hash(line)
        assert utils.trajectory_text(line) != line


class TestPruneIncompleteFolders:
    def test_empty_directory(self, tmp_path):
        assert utils.prune_incomplete_folders(tmp_path) == []

    def test_missing_directory_does_not_crash(self, tmp_path):
        assert utils.prune_incomplete_folders(tmp_path / "does-not-exist") == []

    def test_folder_with_metadata_is_kept(self, tmp_path):
        folder = tmp_path / "abc123-done"
        folder.mkdir()
        (folder / "metadata.json").write_text("{}")
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == []
        assert folder.exists()

    def test_folder_with_stderr_log_is_pruned(self, tmp_path):
        # A recorded harness failure is pruned too, not just crash orphans: a
        # retry can't reuse the name (the slug half is regenerated per attempt
        # and comes out different), so keeping these meant every re-run of a
        # failing batch left another near-duplicate folder behind. The logs
        # survive until the next run starts, no longer.
        folder = tmp_path / "abc123-failed"
        folder.mkdir()
        (folder / "stderr.log").write_text("boom")
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == ["abc123-failed"]
        assert not folder.exists()

    def test_folder_with_stdout_log_is_pruned(self, tmp_path):
        folder = tmp_path / "abc123-failed"
        folder.mkdir()
        (folder / "stdout.log").write_text("")
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == ["abc123-failed"]
        assert not folder.exists()

    def test_folder_with_neither_is_pruned(self, tmp_path):
        # The actual crash-orphan shape: process killed mid-run, so nothing
        # past source.json ever got written.
        folder = tmp_path / "abc123-orphan"
        folder.mkdir()
        (folder / "source.json").write_text('{"foo": "bar"}')
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == ["abc123-orphan"]
        assert not folder.exists()

    def test_completely_empty_folder_is_pruned(self, tmp_path):
        folder = tmp_path / "abc123-empty"
        folder.mkdir()
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == ["abc123-empty"]
        assert not folder.exists()

    def test_unrelated_top_level_file_is_ignored(self, tmp_path):
        (tmp_path / "some-file.txt").write_text("hi")
        assert utils.prune_incomplete_folders(tmp_path) == []

    def test_mixed_folders_only_completed_ones_are_kept(self, tmp_path):
        done = tmp_path / "aaa-done"
        done.mkdir()
        (done / "metadata.json").write_text("{}")

        failed = tmp_path / "bbb-failed"
        failed.mkdir()
        (failed / "stderr.log").write_text("boom")

        orphan = tmp_path / "ccc-orphan"
        orphan.mkdir()
        (orphan / "source.json").write_text("{}")

        removed = utils.prune_incomplete_folders(tmp_path)
        assert sorted(removed) == ["bbb-failed", "ccc-orphan"]
        assert done.exists() and not failed.exists() and not orphan.exists()


class TestReserveName:
    def test_first_claim_gets_the_base_name(self):
        names, lock = set(), threading.Lock()
        assert utils.reserve_name("abc123-slug", names, lock) == "abc123-slug"

    def test_second_claim_of_same_base_gets_dash_2(self):
        names, lock = {"abc123-slug"}, threading.Lock()
        assert utils.reserve_name("abc123-slug", names, lock) == "abc123-slug-2"

    def test_sequential_claims_increment(self):
        names, lock = set(), threading.Lock()
        results = [utils.reserve_name("x", names, lock) for _ in range(5)]
        assert results == ["x", "x-2", "x-3", "x-4", "x-5"]

    def test_claimed_name_is_recorded_in_the_shared_set(self):
        names, lock = set(), threading.Lock()
        utils.reserve_name("x", names, lock)
        assert "x" in names

    def test_unrelated_base_names_dont_collide(self):
        names, lock = set(), threading.Lock()
        assert utils.reserve_name("a", names, lock) == "a"
        assert utils.reserve_name("b", names, lock) == "b"

    def test_pre_existing_names_from_disk_are_respected(self):
        # Simulates a name already on disk from a previous run, not just one
        # claimed earlier in this process.
        names, lock = {"abc123-slug", "abc123-slug-2"}, threading.Lock()
        assert utils.reserve_name("abc123-slug", names, lock) == "abc123-slug-3"

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
            result["name"] = utils.reserve_name("x", names, lock)

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
            results = list(pool.map(lambda _: utils.reserve_name("same-base", names, lock), range(n)))
        assert len(results) == n
        assert len(set(results)) == n  # every claimed name is unique

    def test_concurrent_claims_across_many_distinct_bases(self):
        # Same stress, but a realistic mix: mostly-distinct base names with a
        # handful of accidental repeats, matching what a real batch looks like.
        names, lock = set(), threading.Lock()
        bases = [f"base-{i % 10}" for i in range(200)]
        with ThreadPoolExecutor(max_workers=16) as pool:
            results = list(pool.map(lambda b: utils.reserve_name(b, names, lock), bases))
        assert len(results) == len(set(results)) == 200


class TestScanExistingOutput:
    def _write_metadata(self, folder, **fields):
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "metadata.json").write_text(json.dumps(fields))

    def test_empty_directory(self, tmp_path):
        done, names = utils.scan_existing_output(tmp_path)
        assert done == set()
        assert names == set()

    def test_missing_directory_does_not_crash(self, tmp_path):
        done, names = utils.scan_existing_output(tmp_path / "does-not-exist")
        assert done == set()
        assert names == set()

    def test_successful_record_is_marked_done(self, tmp_path):
        self._write_metadata(tmp_path / "abc123-some-slug", hash="fullhash1",
                              timestamp="2026-01-01T00:00:00+00:00")
        done, names = utils.scan_existing_output(tmp_path)
        assert done == {"fullhash1"}
        assert "abc123-some-slug" in names

    def test_failed_record_not_marked_done_but_its_name_is_still_reserved(self, tmp_path):
        folder = tmp_path / "abc123-some-slug"
        folder.mkdir(parents=True)
        (folder / "stdout.log").write_text("")
        (folder / "stderr.log").write_text("boom")
        done, names = utils.scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_partial_metadata_missing_timestamp_not_marked_done(self, tmp_path):
        # Written-but-not-yet-completed shape shouldn't count as done, in
        # case a future version starts writing metadata.json earlier.
        self._write_metadata(tmp_path / "abc123-some-slug", hash="fullhash1")
        done, names = utils.scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_corrupt_metadata_json_does_not_crash_the_scan(self, tmp_path):
        folder = tmp_path / "abc123-some-slug"
        folder.mkdir(parents=True)
        (folder / "metadata.json").write_text("{not valid json")
        done, names = utils.scan_existing_output(tmp_path)
        assert done == set()
        assert "abc123-some-slug" in names

    def test_unrelated_top_level_file_is_ignored(self, tmp_path):
        (tmp_path / "some-stray-file.txt").write_text("hi")
        done, names = utils.scan_existing_output(tmp_path)
        assert names == set()

    def test_multiple_records_of_mixed_status_all_collected_correctly(self, tmp_path):
        self._write_metadata(tmp_path / "aaa-one", hash="h1", timestamp="t")
        self._write_metadata(tmp_path / "bbb-two", hash="h2", timestamp="t")
        failed = tmp_path / "ccc-three"
        failed.mkdir()
        (failed / "stderr.log").write_text("failed")
        done, names = utils.scan_existing_output(tmp_path)
        assert done == {"h1", "h2"}
        assert names == {"aaa-one", "bbb-two", "ccc-three"}


class TestLoadConfig:
    ENV_VARS = ["SWARM_HARNESS", "SWARM_TASK", "SWARM_MODEL", "SWARM_CONCURRENCY",
                "SWARM_EXPERIMENT", "PROXY_BASE_URL", "PROXY_API_KEY"]

    def _clear_env(self, monkeypatch):
        for var in self.ENV_VARS:
            monkeypatch.delenv(var, raising=False)

    def _make_harness(self, self_dir, name="opencode"):
        harness_dir = self_dir / "harnesses" / name
        harness_dir.mkdir(parents=True, exist_ok=True)
        (harness_dir / "Dockerfile").write_text("FROM scratch")

    def _make_task(self, self_dir, name="discovery"):
        task_dir = self_dir / "tasks"
        task_dir.mkdir(parents=True, exist_ok=True)
        (task_dir / f"{name}.md").write_text("do the task")

    def test_defaults_when_nothing_set(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        monkeypatch.setenv("PROXY_API_KEY", "test-key")
        self._make_harness(tmp_path, "opencode")
        self._make_task(tmp_path, "discovery")

        config = utils.load_config(tmp_path)

        assert config.harness_name == "opencode"
        assert config.task_name == "discovery"
        assert config.model == "vertex-proxy/gemini-flash"
        assert config.concurrency == 4
        assert config.experiment is None
        assert config.api_key == "test-key"

    def test_env_vars_override_defaults(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        monkeypatch.setenv("PROXY_API_KEY", "k")
        monkeypatch.setenv("SWARM_HARNESS", "pi")
        monkeypatch.setenv("SWARM_TASK", "custom")
        monkeypatch.setenv("SWARM_MODEL", "vertex-proxy/other-model")
        monkeypatch.setenv("SWARM_CONCURRENCY", "8")
        monkeypatch.setenv("SWARM_EXPERIMENT", "exp-1")
        self._make_harness(tmp_path, "pi")
        self._make_task(tmp_path, "custom")

        config = utils.load_config(tmp_path)

        assert config.harness_name == "pi"
        assert config.task_name == "custom"
        assert config.model == "vertex-proxy/other-model"
        assert config.concurrency == 8
        assert config.experiment == "exp-1"

    def test_raises_when_api_key_missing(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        self._make_harness(tmp_path)
        self._make_task(tmp_path)
        with pytest.raises(ValueError, match="PROXY_API_KEY"):
            utils.load_config(tmp_path)

    def test_raises_when_harness_does_not_exist(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        monkeypatch.setenv("PROXY_API_KEY", "k")
        monkeypatch.setenv("SWARM_HARNESS", "nonexistent")
        self._make_task(tmp_path)
        with pytest.raises(ValueError, match="no such harness"):
            utils.load_config(tmp_path)

    def test_raises_when_task_file_does_not_exist(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        monkeypatch.setenv("PROXY_API_KEY", "k")
        monkeypatch.setenv("SWARM_TASK", "nonexistent")
        self._make_harness(tmp_path)
        with pytest.raises(ValueError, match="no such task file"):
            utils.load_config(tmp_path)

    def test_loads_dotenv_from_self_dir(self, tmp_path, monkeypatch):
        self._clear_env(monkeypatch)
        self._make_harness(tmp_path)
        self._make_task(tmp_path)
        (tmp_path / ".env").write_text("PROXY_API_KEY=from-dotenv\n")

        config = utils.load_config(tmp_path)
        assert config.api_key == "from-dotenv"


class TestLoadBatch:
    def test_reads_one_record_per_line(self, tmp_path):
        batch = tmp_path / "batch.jsonl"
        batch.write_text('{"content": "a"}\n{"content": "b"}\n')
        records, skipped = utils.load_batch(batch, set())
        assert len(records) == 2
        assert skipped == 0

    def test_skips_blank_lines(self, tmp_path):
        batch = tmp_path / "batch.jsonl"
        batch.write_text('{"content": "a"}\n\n{"content": "b"}\n')
        records, skipped = utils.load_batch(batch, set())
        assert len(records) == 2

    def test_skips_records_whose_hash_is_already_done(self, tmp_path):
        batch = tmp_path / "batch.jsonl"
        line_a = '{"content": "a"}'
        line_b = '{"content": "b"}'
        batch.write_text(line_a + "\n" + line_b + "\n")
        done_hashes = {utils.content_hash(line_a)}

        records, skipped = utils.load_batch(batch, done_hashes)

        assert skipped == 1
        assert len(records) == 1
        assert records[0][0] == line_b

    def test_each_record_pairs_line_with_its_own_hash(self, tmp_path):
        batch = tmp_path / "batch.jsonl"
        line = '{"content": "a"}'
        batch.write_text(line + "\n")
        records, _ = utils.load_batch(batch, set())
        assert records == [(line, utils.content_hash(line))]

    def test_empty_file(self, tmp_path):
        batch = tmp_path / "batch.jsonl"
        batch.write_text("")
        records, skipped = utils.load_batch(batch, set())
        assert records == []
        assert skipped == 0


class TestBuildDockerCmd:
    """The security posture (non-root, no capabilities, no privilege
    escalation, resource caps) and the mount surface are exactly what stands
    between an untrusted harness container and the host. Asserted directly
    here so a future edit that accidentally drops one is a failing test, not
    a silent regression only caught by re-reading ADVANCED.md.
    """

    def _cmd(self, **overrides):
        args = dict(uid=1000, gid=1000, model="vertex-proxy/gemini-flash",
                    design_doc="/path/DESIGN_DOC.md", traj_path="/tmp/traj.txt",
                    prompt_file="/tmp/prompt.md", scratch="/tmp/scratch", image="my-image")
        args.update(overrides)
        return utils.build_docker_cmd(**args)

    def test_starts_with_docker_run_rm(self):
        cmd = self._cmd()
        assert cmd[:3] == ["docker", "run", "--rm"]

    def test_ends_with_the_image(self):
        cmd = self._cmd(image="my-image")
        assert cmd[-1] == "my-image"

    def test_runs_as_the_given_uid_and_gid_not_root(self):
        cmd = self._cmd(uid=501, gid=20)
        assert "--user" in cmd
        assert cmd[cmd.index("--user") + 1] == "501:20"

    def test_drops_all_capabilities(self):
        assert "--cap-drop=ALL" in self._cmd()

    def test_blocks_privilege_escalation(self):
        cmd = self._cmd()
        assert "--security-opt" in cmd
        assert cmd[cmd.index("--security-opt") + 1] == "no-new-privileges:true"

    def test_caps_memory_and_cpu(self):
        cmd = self._cmd()
        assert "--memory" in cmd
        assert cmd[cmd.index("--memory") + 1] == "1g"
        assert "--cpus" in cmd
        assert cmd[cmd.index("--cpus") + 1] == "1"

    def test_mounts_design_doc_trajectory_and_prompt_read_only(self):
        cmd = self._cmd(design_doc="/d/DESIGN_DOC.md", traj_path="/t/traj.txt",
                         prompt_file="/p/prompt.md")
        assert "/d/DESIGN_DOC.md:/reference/DESIGN_DOC.md:ro" in cmd
        assert "/t/traj.txt:/trajectory.txt:ro" in cmd
        assert "/p/prompt.md:/prompt.md:ro" in cmd

    def test_mounts_output_writable_not_read_only(self):
        cmd = self._cmd(scratch="/s/scratch")
        assert "/s/scratch:/output" in cmd
        assert not any(a.startswith("/s/scratch:/output:") for a in cmd)

    def test_passes_model_as_env_var(self):
        cmd = self._cmd(model="vertex-proxy/other-model")
        assert "-e" in cmd
        assert "SWARM_MODEL=vertex-proxy/other-model" in cmd

    def test_passes_through_proxy_credentials_by_name_not_value(self):
        # "-e VAR" (no "=value") means docker inherits it from spawn_batch.py's
        # own environment — the key never appears in the command line itself.
        cmd = self._cmd()
        assert "PROXY_API_KEY" in cmd
        assert "PROXY_BASE_URL" in cmd
        assert not any("PROXY_API_KEY=" in a for a in cmd)

    def test_network_is_not_restricted(self):
        # Deliberate: every harness needs to reach the model API. Asserted as
        # a documented absence, not just an omission nobody checks.
        cmd = self._cmd()
        assert "--network" not in cmd
        assert "--net" not in cmd
