import os
import openai

openai.api_key = os.getenv("sk-...DSIA")


def run_llm(prompt):
    if openai.api_key:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content
    else:
        return "[LOCAL MODE] " + prompt[:500]
