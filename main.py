import os
import re
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = """You are a professional workplace assistant that writes emails and updates.

Rules:
1. Max 3 sentences total. Never write a 4th sentence.
2. Don't apologize more than once, and only if it's actually needed.
3. No dramatic language ("I deeply regret", "devastated", "unforeseen circumstances beyond our control").
4. No exclamation points.
5. Put the actual fact/update in sentence 1. Use sentence 2 for a detail if needed. Sentence 3 only for a next step - don't add one just to fill space.
6. No "Dear Team" greetings or "Best regards" sign-offs unless asked for a full email.
7. When unsure, go shorter, not longer.

Tone: calm, direct, professional. Like a competent coworker giving a quick update, not a customer service script.
"""


def ask(user_input):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ],
        temperature=0.4,
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()


def count_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return len([p for p in parts if p])


TEST_CASES = [
    "Write an update telling the client their project is delayed by two weeks due to a supplier issue.",
    "The server crashed at 3am and took down the whole site for 20 minutes. Write an incident update.",
    "Tell my manager I finished the report early and it's ready for review.",
    "We lost the client's biggest account to a competitor. Break the news to the team gently.",
    "Just say hi and ask how the meeting went.",
]

if __name__ == "__main__":
    if not os.environ.get("GROQ_API_KEY"):
        raise SystemExit("Set the GROQ_API_KEY environment variable first.")

    for i, case in enumerate(TEST_CASES, start=1):
        output = ask(case)
        sentences = count_sentences(output)
        status = "PASS" if sentences <= 3 else "FAIL"
        print(f"\n--- Test {i} [{status}] ({sentences} sentences) ---")
        print(f"Input:  {case}")
        print(f"Output: {output}")
