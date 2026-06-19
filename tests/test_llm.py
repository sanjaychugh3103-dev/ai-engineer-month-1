from src.llm import call_llm


def test_call_llm_basic():
    result = call_llm("Say hi in one word.")

    assert result.text, "text should be non-empty"
    assert result.input_tokens > 0
    assert result.output_tokens > 0
    assert result.latency_seconds > 0
