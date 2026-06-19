import json
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def embed(texts: list[str], model: str = "text-embedding-3-small") -> list[list[float]]:
    """Return embedding vectors for a list of texts."""
    response = client.embeddings.create(model=model, input=texts)
    return [item.embedding for item in response.data]

if __name__ == "__main__":
    sentences = [
        "I love making pasta from scratch",
        "The recipe calls for fresh basil",
        "I was a vegetarian for 7 years",
        "I should be eating more vegetarian food",
        "I need to eat oily fish 3 days per week",
        "I need to make sure my children develop cooking skills",
        "Cooking is an important life skill",
        "I eat too much chicken",
        "I love a nice salad",
        "I miss my mum's smile and cooking",
        "Everyone should learn some basic programming",
        "I wish I was a Python expert",
        "Programming can solve many problems of life",
        "Programming is difficult",
        "Programming take a lot of hard work to learn",
        "Everyone can be a programmer",
        "Programming has changed with AI",
        "Programmers are problem solvers",
        "I wish my children learnt programming",
        "I wish I had stayed in technology when I was a teenager",
        "London weather is unpredictable",
        "Weather can have a huge impact on state of mind",
        "Everyway you go always take the weather with you",
        "Weather or wither",
        "I love Thailand weather",
        "Finland is sold cold in the winter",
        "If there was no winter, summer would not be fun",
        "Summer and Ice cream",
        "I don't like Indian summers, it's too hot",
        "I love summer, only when it is between 18 and 28 degrees",
        "My favourite holiday destination is Thailand",
        "I need to travel more",
        "I love France, I wish I could speak French",
        "French is a beautiful language",
        "Travel broadens your perspective about life",
        "Travel is good for the soul",
        "I would love to go to Japan, but at least for 3 months",
        "I love travelling within UK, especially down south - Devon and Cornwall",
        "I wish I was rich",
        "I wish I had a holiday home in France",
        "Life, oh Life, oh Life",
        "What is Life without laugher",
        "Life is full of challenges",
        "If you are always happy, how will you appreciate happiness",
        "A bit of sadness in life is required to appreciate happiness",
        "What happens after death",
        "Death is inevitable",
        "We should not be scared of death",
        "I am happy when my family is happy",
        "If you change your thinking, you can change your life",
    ]

    vectors = embed(sentences)
    print(f"Number of vectors: {len(vectors)}")
    print(f"Dimension of each: {len(vectors[0])}")
    for i, vec in enumerate(vectors):
        print(f"Vector {i}: {vec[:10]}")

    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    records = [{"text": s, "embedding": v} for s, v in zip(sentences, vectors)]
    with open(data_dir / "embeddings.json", "w") as f:
        json.dump(records, f, indent=2)

    print(f"Saved {len(records)} embeddings to data/embeddings.json")
