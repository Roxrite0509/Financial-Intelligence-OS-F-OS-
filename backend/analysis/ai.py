import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("sk-...j7wA"))


def explain_stock_move(symbol, return_pct, volatility):
    prompt = f"""
    Explain why the bank stock {symbol} moved today.

    Return: {return_pct}%
    Volatility: {volatility}%

    Explain clearly in simple language for investors.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


def explain_stock_move(symbol, return_pct, volatility):
    direction = "rose" if return_pct > 0 else "fell"

    return (
        f"{symbol} {direction} {abs(return_pct)}% recently. "
        f"Volatility remains {'low' if volatility < 2 else 'elevated'}, "
        f"suggesting {'stable institutional interest' if volatility < 2 else 'higher trading activity'}. "
        f"Indian banking stocks typically react to RBI policy signals and bond yield expectations."
    )
