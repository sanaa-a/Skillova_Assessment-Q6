# Final Report:AI Chatbots & Prompt Engineering

## The Problem

When you ask a generative AI to write a quick email, it often responds with something long and overly formal. It gives five paragraphs when you needed two sentences as the AI has no sense of "keep it short". The goal of this project was to control that behavior using prompt engineering, without changing the AI model itself.

## The Approach

I used Groq's API and wrote a Python script (Used some code from my previous project) that sends every request through two layers of instructions:

- **System Prompt** — a fixed set of rules the AI follows for the entire conversation. These are set once and never shown to the end user. These are the AI's "job description". In my script this is where I placed all the rules: max 3 sentences, no exclamation points, no dramatic phrases, etc.
- **User Prompt** — is just the actual request for that specific moment. The prompt a normal person would type in, like "tell my manager the report is ready". This changes every single time. So in the script, the system prompt stays fixed across all 5 of my test cases, but the user prompt is different for each one.

My key finding: Vague instructions don't work. My first attempt just told the AI to "be concise and professional" , and it mostly ignored that and kept writing long responses. What actually worked was being extremely specific. So I did a numbered list of hard rules instead of a general request:

- Maximum 3 sentences, no exceptions
- No exclamation points
- No dramatic phrases like "I deeply regret" or "unforeseen circumstances"
- State the fact in sentence 1, not buried at the end

These specific and measurable rules constrained the AI's behavior.

## Testing

I tested the final system prompt against 5 different scenarios, including intentionally emotional or bad news situations that were on purpose to see if the AI would write long or dramatic responses (e.g. "we lost the client's biggest account"). I wrote a small check in the script that counts sentences automatically, rather than eyeballing the output.

**Result:** All 5 test cases stayed within the 3-sentence limit.

## A Limitation in my Opinion

The last test was a casual "just say hi and ask how the meeting went" — still came back sounding like a formal status update rather than a casual message. The AI followed the *length* rule correctly but couldn't loosen its *tone*, because the system prompt gave it no room to be casual. This shows that the more rigid the constraints, the more consistent the format, but the less natural the AI sounds in situations that call for a lighter message.

## Other Methods I Considered 

Before landing on the system prompt approach, I looked into a few other ways to control the AI's output length:

Just cutting the text off in Python (post-processing)- Like, let the AI ramble and then cut it down to the first 3 sentences with code. This seemed easier at first, but it's kind of a bad idea as I ended up with cutting mid-sentence sometimes, and it doesn't actually fix the dramatic tone, it just hides it. 

Turning down the max_tokens setting- The API lets me cap how many tokens the AI is allowed to generate. I tried this early on and it does shorten things, but it's messy. It just cuts the response off wherever the token limit hits, which can end mid-sentence and doesn't actually teach the AI to plan for 3 sentences, it just runs out of space.

Fine-tuning the model- This is basically retraining the AI on a bunch of examples of short, professional responses. I didn't even attempt this as it is way overkill for this. It needs a dataset, GPU time, and way more setup.

**My solution was best** using the system prompt because it's basically free (no extra training, no extra API calls), you can test and tweak it in seconds, and it actually changes how the AI reasons about the response before it even starts writing, instead of just patching the output afterward.