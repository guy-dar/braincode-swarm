"""Regression test for a real production incident: AnthropicClient.generate() used to call
client.messages.create() (non-streaming), which the Anthropic SDK refuses outright once
max_tokens is high enough that it estimates generation could exceed 10 minutes for the model —
raised client-side, before any network request, as "Streaming is required for operations that
may take longer than 10 minutes." This made every single Shaper/Critic call using a large
max_tokens fail instantly (all 100 bootstrap attempts within the same second in one real run).
Fixed by switching to client.messages.stream(...).get_final_message(), which the SDK accepts
regardless of max_tokens and which returns the same Message shape .create() did.

Uses a fake SDK client (bypassing AnthropicClient._ensure_client()'s lazy import/API-key check
entirely) so this test needs no real API key and makes no network call."""
from braincode_loop.llm.anthropic_client import AnthropicClient


class _FakeBlock:
    def __init__(self, text):
        self.type = "text"
        self.text = text


class _FakeUsage:
    def __init__(self, input_tokens, output_tokens):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens


class _FakeMessage:
    def __init__(self, text, input_tokens=10, output_tokens=20):
        self.content = [_FakeBlock(text)]
        self.usage = _FakeUsage(input_tokens, output_tokens)


class _FakeStreamContext:
    def __init__(self, final_message):
        self._final_message = final_message

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        return False

    def get_final_message(self):
        return self._final_message


class _FakeMessagesAPI:
    def __init__(self, final_message):
        self._final_message = final_message
        self.stream_calls = []
        self.create_calls = []

    def stream(self, **kwargs):
        self.stream_calls.append(kwargs)
        return _FakeStreamContext(self._final_message)

    def create(self, **kwargs):
        # If this is ever called, generate() regressed back to the non-streaming path that
        # caused the real incident this test guards against.
        self.create_calls.append(kwargs)
        raise AssertionError("AnthropicClient.generate() must use messages.stream(), not messages.create()")


class _FakeAnthropicSDKClient:
    def __init__(self, final_message):
        self.messages = _FakeMessagesAPI(final_message)


def test_generate_uses_streaming_not_create():
    client = AnthropicClient(model="claude-sonnet-5")
    fake_sdk = _FakeAnthropicSDKClient(_FakeMessage("hello world"))
    client._client = fake_sdk  # bypass the lazy _ensure_client() import/API-key check

    result = client.generate(system="sys prompt", user="user prompt", max_tokens=32000, temperature=0.5)

    assert len(fake_sdk.messages.stream_calls) == 1
    assert fake_sdk.messages.create_calls == []
    call = fake_sdk.messages.stream_calls[0]
    assert call["model"] == "claude-sonnet-5"
    assert call["max_tokens"] == 32000
    assert call["system"] == "sys prompt"
    assert call["messages"] == [{"role": "user", "content": "user prompt"}]
    assert "temperature" not in call  # documented: the Messages API dropped temperature entirely

    assert result.text == "hello world"
    assert result.input_tokens == 10
    assert result.output_tokens == 20
    assert result.provider == "anthropic"
    assert result.model == "claude-sonnet-5"


def test_generate_concatenates_only_text_blocks():
    client = AnthropicClient(model="claude-sonnet-5")
    message = _FakeMessage("ignored")
    message.content = [_FakeBlock("part one. "), _FakeBlock("part two.")]
    fake_sdk = _FakeAnthropicSDKClient(message)
    client._client = fake_sdk

    result = client.generate(system="s", user="u", max_tokens=1000, temperature=0.2)

    assert result.text == "part one. part two."
