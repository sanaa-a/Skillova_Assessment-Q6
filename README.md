# Skillova Assessment- Question 6

Forces a generative Groq AI to always respond in 3 sentences or
fewer, in a calm professional tone, with no dramatic filler. No matter what the user input is

## How to run

1. Get a free API key at https://console.groq.com/keys
2. Install the dependency:
pip install groq
3. Set your key as an environment variable (PowerShell):
$env:GROQ_API_KEY="your_key_here"
4. Run:
python main.py

This runs 5 test prompts, including ones designed to obtain a long, dramatic
response, and prints each output along with a sentence count and PASS/FAIL
against the 3-sentence limit.

## Files

- `main.py` - the script, system prompt, and test cases