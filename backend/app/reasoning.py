from backend.app.llm import run_llm


def generate_insights(evidence):
    prompt = f"""
Market: {evidence['market']}
Policy: {evidence['policy']}
News: {evidence['news']}

Give:
1. Key insight
2. Key risk
3. One-line verdict
"""
    return run_llm(prompt)
