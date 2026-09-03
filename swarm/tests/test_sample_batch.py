"""Tests for sample_batch.py.

Weighted towards the exclusion logic, because that's the part whose failure is
silent: a sampler that re-draws a processed record produces a batch that looks
fine, runs fine, and quietly pays for work already done.
"""
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import sample_batch


def record(content, rec_id=None):
    obj = {"content": content}
    if rec_id is not None:
        obj["id"] = rec_id
    return json.dumps(obj)


def turns(topic="hello"):
    return f"<|user|>\n{topic}\n<|assistant|>\nsure, {topic}"


def write_jsonl(path, lines):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(l + "\n" for l in lines))


def run(tmp_path, extra=None, data=None, count=10):
    """Invoke main() against a self-contained tree, returning the drawn records."""
    args = ["-n", str(count),
            "--data", str(data or (tmp_path / "data")),
            "--output-dir", str(tmp_path / "output"),
            "--batches-dir", str(tmp_path / "batches")]
    assert sample_batch.main(args + (extra or [])) == 0
    written = sorted((tmp_path / "batches").glob("batch-*.jsonl"))[-1]
    return [json.loads(l) for l in written.read_text().splitlines()]


class TestFilters:
    def test_draws_eligible_records(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns(f"t{i}"), f"id-{i}") for i in range(5)])
        assert len(run(tmp_path)) == 5

    def test_skips_records_without_turn_tags(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns("kept")), record("just a plain string")])
        drawn = run(tmp_path)
        assert [r["content"] for r in drawn] == [turns("kept")]

    def test_no_require_turns_keeps_them(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns("kept")), record("just a plain string")])
        assert len(run(tmp_path, ["--no-require-turns"])) == 2

    def test_length_bounds(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns("x" * 500)), record(turns("y"))])
        drawn = run(tmp_path, ["--max-chars", "100"])
        assert len(drawn) == 1 and "y" in drawn[0]["content"]
        drawn = run(tmp_path, ["--min-chars", "100"])
        assert len(drawn) == 1 and "x" * 500 in drawn[0]["content"]

    def test_latin_only(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns("plain ascii")), record(turns("日本語")),
                     record(turns("naïve café — 20°"))])
        drawn = run(tmp_path, ["--latin-only"])
        contents = [r["content"] for r in drawn]
        assert len(contents) == 2
        assert not any("日本語" in c for c in contents)

    def test_skips_malformed_and_empty(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns("kept")), "{not json", "[1,2,3]",
                     json.dumps({"content": "   "}), json.dumps({"no_content": 1})])
        assert len(run(tmp_path)) == 1

    def test_drops_duplicates_within_the_source(self, tmp_path):
        line = record(turns("same"), "id-1")
        write_jsonl(tmp_path / "data" / "src.jsonl", [line, line, line])
        assert len(run(tmp_path)) == 1


class TestExclusion:
    def test_excludes_by_hash_from_output_metadata(self, tmp_path):
        done, fresh = record(turns("done")), record(turns("fresh"))
        write_jsonl(tmp_path / "data" / "src.jsonl", [done, fresh])
        folder = tmp_path / "output" / "aaaaaa-done"
        folder.mkdir(parents=True)
        (folder / "metadata.json").write_text(json.dumps(
            {"hash": sample_batch.content_hash(done), "timestamp": "now"}))

        drawn = run(tmp_path)
        assert [r["content"] for r in drawn] == [json.loads(fresh)["content"]]

    def test_excludes_by_id_when_the_line_differs(self, tmp_path):
        """The case a content hash cannot catch: same trajectory, re-serialized."""
        original = json.dumps({"id": "x-1", "content": turns("same")})
        reoffered = json.dumps({"content": turns("same"), "id": "x-1", "extra": 1})
        assert sample_batch.content_hash(original) != sample_batch.content_hash(reoffered)
        write_jsonl(tmp_path / "data" / "src.jsonl", [reoffered])
        folder = tmp_path / "output" / "aaaaaa-done"
        folder.mkdir(parents=True)
        (folder / "source.json").write_text(original)

        assert run(tmp_path) == []

    def test_excludes_records_that_failed(self, tmp_path):
        failed = record(turns("failed"), "id-1")
        write_jsonl(tmp_path / "data" / "src.jsonl", [failed])
        folder = tmp_path / "failures" / "aaaaaa"
        folder.mkdir(parents=True)
        (folder / "failure.json").write_text(json.dumps(
            {"hash": sample_batch.content_hash(failed)}))

        assert run(tmp_path) == []

    def test_excludes_records_already_in_a_batch_file(self, tmp_path):
        drawn_before = record(turns("already drawn"), "id-1")
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [drawn_before, record(turns("new"), "id-2")])
        write_jsonl(tmp_path / "batches" / "batch-01.jsonl", [drawn_before])

        drawn = run(tmp_path)
        assert [r["id"] for r in drawn] == ["id-2"]

    def test_no_exclude_disables_it(self, tmp_path):
        done = record(turns("done"), "id-1")
        write_jsonl(tmp_path / "data" / "src.jsonl", [done])
        write_jsonl(tmp_path / "batches" / "batch-01.jsonl", [done])
        assert len(run(tmp_path, ["--no-exclude"])) == 1


class TestOutputPath:
    def test_takes_the_next_free_number(self, tmp_path):
        batches = tmp_path / "batches"
        write_jsonl(batches / "batch-01.jsonl", [])
        write_jsonl(batches / "batch-02.jsonl", [])
        write_jsonl(batches / "batch-07.jsonl", [])
        assert sample_batch.next_batch_path(batches).name == "batch-03.jsonl"

    def test_first_batch_when_none_exist(self, tmp_path):
        (tmp_path / "batches").mkdir()
        assert sample_batch.next_batch_path(tmp_path / "batches").name == "batch-01.jsonl"

    def test_ignores_non_numeric_names(self, tmp_path):
        batches = tmp_path / "batches"
        write_jsonl(batches / "batch-retry.jsonl", [])
        assert sample_batch.next_batch_path(batches).name == "batch-01.jsonl"

    def test_writes_to_an_explicit_out_path(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl", [record(turns("a"))])
        dest = tmp_path / "elsewhere" / "custom.jsonl"
        dest.parent.mkdir()
        assert sample_batch.main([
            "-n", "1", "--data", str(tmp_path / "data"), "--out", str(dest),
            "--output-dir", str(tmp_path / "output"),
            "--batches-dir", str(tmp_path / "batches")]) == 0
        assert len(dest.read_text().splitlines()) == 1


class TestSources:
    def test_accepts_a_file_a_dir_and_a_glob(self, tmp_path):
        write_jsonl(tmp_path / "data" / "nested" / "a.jsonl", [record(turns("a"))])
        write_jsonl(tmp_path / "data" / "b.jsonl", [record(turns("b"))])
        # --no-exclude on the later draws: without it each one would correctly
        # skip what the previous draw already wrote to batches/.
        assert len(run(tmp_path)) == 2                            # dir, recursive
        assert len(run(tmp_path, ["--no-exclude"],
                       data=tmp_path / "data" / "b.jsonl")) == 1   # single file
        assert len(run(tmp_path, ["--no-exclude"],
                       data=str(tmp_path / "data" / "*.jsonl"))) == 1   # glob, not recursive

    def test_a_file_named_twice_is_read_once(self, tmp_path):
        path = tmp_path / "data" / "a.jsonl"
        write_jsonl(path, [record(turns("a"))])
        args = ["-n", "10", "--data", str(path), str(path),
                "--output-dir", str(tmp_path / "output"),
                "--batches-dir", str(tmp_path / "batches")]
        assert sample_batch.main(args) == 0
        written = (tmp_path / "batches" / "batch-01.jsonl").read_text().splitlines()
        assert len(written) == 1

    def test_no_sources_is_an_error(self, tmp_path, capsys):
        assert sample_batch.main([
            "--data", str(tmp_path / "nothing-here"),
            "--output-dir", str(tmp_path / "output"),
            "--batches-dir", str(tmp_path / "batches")]) == 1


class TestSampling:
    def test_same_seed_draws_the_same_records(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns(f"t{i}"), f"id-{i}") for i in range(50)])
        first = run(tmp_path, ["--seed", "7", "--no-exclude"], count=5)
        second = run(tmp_path, ["--seed", "7", "--no-exclude"], count=5)
        assert [r["id"] for r in first] == [r["id"] for r in second]

    def test_default_seed_differs_per_destination(self, tmp_path):
        """Derived from the filename, so consecutive batches don't collide."""
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns(f"t{i}"), f"id-{i}") for i in range(200)])
        first = run(tmp_path, ["--no-exclude"], count=5)
        second = run(tmp_path, ["--no-exclude"], count=5)
        assert [r["id"] for r in first] != [r["id"] for r in second]

    def test_requesting_more_than_exists_draws_everything(self, tmp_path):
        write_jsonl(tmp_path / "data" / "src.jsonl",
                    [record(turns(f"t{i}"), f"id-{i}") for i in range(3)])
        assert len(run(tmp_path, count=100)) == 3

    def test_hash_matches_the_pipelines_own(self, tmp_path):
        """Duplicated from utils on purpose (no dependencies) — so pin it."""
        import utils
        line = record(turns("x"), "id-1")
        assert sample_batch.content_hash(line) == utils.content_hash(line)
