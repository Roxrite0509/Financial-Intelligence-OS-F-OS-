import os
from openai import OpenAI

client = None
if os.getenv("OPENAI_API_KEY"):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyst_llm(evidence):
    return f"""
Market: {evidence['market']}
Policy: {evidence['policy']}
News: {evidence['news']}

Give key insights & risks.
"""


def run_llm(prompt: str):
    if not client:
        return "LLM unavailable. Showing data only."

    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a banking analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return res.choices[0].message.content
    except Exception as e:
        return f"LLM error: {str(e)}"
