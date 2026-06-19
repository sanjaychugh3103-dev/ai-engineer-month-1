import tiktoken

def count_tokens(text: str, model: str = "gpt-4o") -> int:
    """Return the number of tokens `text` becomes for the given model."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))


def estimate_cost(text: str, model: str = "gpt-4o",
                  input_cost_per_1m: float = 2.50) -> float:
    """Rough cost estimate for sending `text` as input. Returns USD."""
    tokens = count_tokens(text, model)
    return (tokens / 1_000_000) * input_cost_per_1m


if __name__ == "__main__":
    samples = [
        "Hello, world!",
        "The quick brown fox jumps over the lazy dog.",
        "anthropomorphic disestablishmentarianism",
        "🚀 Let's go! 🎉",
        "你好，世界",
        "def hello(name): return f'hello, {name}'",
    ]
    for s in samples:
        n = count_tokens(s)
        c = estimate_cost(s)
        print(f"{n:>3} tokens  ${c:.6f}  | {s!r}")