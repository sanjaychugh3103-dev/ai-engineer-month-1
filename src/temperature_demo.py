import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT = "Why is Paris the capital of France"

def run(temperature: float, n_runs: int = 5) -> list[str]:
    results = []
    for _ in range(n_runs):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": PROMPT}],
            temperature=temperature,
            max_tokens=60,
        )
        results.append(response.choices[0].message.content.strip())
    return results

if __name__ == "__main__":
    for t in [0.0, 0.7, 1.5]:
        print(f"\n=== temperature = {t} ===")
        for i, line in enumerate(run(t), 1):
            print(f"{i}. {line}")