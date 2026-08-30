"""Tests for utils.py: the naming logic (content hash, slug, folder name).

generate_slug() is the one function that talks to a real model in production;
here it's tested against a mocked litellm.completion so these run offline,
deterministically, and cover failure shapes (including the exact "no choices"
malformed-response shape hit once during development) without spending real
tokens or needing credentials.
"""
from unittest.mock import MagicMock, patch

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

    def test_folder_with_stderr_log_is_kept(self, tmp_path):
        # A recorded harness failure, not a crash — deliberately preserved
        # for debugging, must never be pruned.
        folder = tmp_path / "abc123-failed"
        folder.mkdir()
        (folder / "stderr.log").write_text("boom")
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == []
        assert folder.exists()

    def test_folder_with_stdout_log_is_kept(self, tmp_path):
        folder = tmp_path / "abc123-failed"
        folder.mkdir()
        (folder / "stdout.log").write_text("")
        removed = utils.prune_incomplete_folders(tmp_path)
        assert removed == []
        assert folder.exists()

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

    def test_mixed_folders_only_orphans_are_removed(self, tmp_path):
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
        assert removed == ["ccc-orphan"]
        assert done.exists() and failed.exists() and not orphan.exists()
