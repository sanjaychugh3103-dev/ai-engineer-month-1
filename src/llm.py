import time
from dataclasses import dataclass
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PRICING = {
    "gpt-4o-mini": (0.15, 0.60),
    "gpt-4o":      (2.50, 10.00),
}

@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int
    latency_seconds: float
    cost_usd: float
    model: str

def call_llm(
    user_message: str,
    system_prompt: str = "You are a helpful assistant.",
    model: str = "gpt-4o",
    temperature: float = 0.7,
) -> LLMResult:
    client = OpenAI()

    start = time.perf_counter()
    response = client.chat.completions.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
    )
    latency = time.perf_counter() - start

    text = response.choices[0].message.content
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens

    input_price, output_price = PRICING.get(model, (0.0, 0.0))
    cost = (input_tokens * input_price + output_tokens * output_price) / 1_000_000

    return LLMResult(
        text=text,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_seconds=latency,
        cost_usd=cost,
        model=model,
    )


if __name__ == "__main__":
    result = call_llm("What is the capital of France?")
    print(f"text:           {result.text}")
    print(f"input tokens:   {result.input_tokens}")
    print(f"output tokens:  {result.output_tokens}")
    print(f"latency:        {result.latency_seconds:.2f}s")
    print(f"cost:           ${result.cost_usd:.7f}")
    print(f"model:          {result.model}")