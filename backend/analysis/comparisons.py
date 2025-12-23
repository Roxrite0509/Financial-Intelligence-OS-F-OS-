import yfinance as yf


# backend/analysis/comparisons.py
def compare_banks(banks: list):
    output = []

    for b in banks:
        output.append({
            "symbol": b["symbol"],
            "price": b.get("price"),
            "return_pct": b.get("return_pct"),
            "volatility": b.get("volatility"),
        })

    return output
