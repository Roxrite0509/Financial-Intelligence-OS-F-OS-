import yfinance as yf
import pandas as pd


def compare_banks(symbols: list[str], period="6mo"):
    result = []

    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period)

        if df.empty:
            continue

        start = df.iloc[0]["Close"]
        end = df.iloc[-1]["Close"]

        returns = ((end - start) / start) * 100
        volatility = df["Close"].pct_change().std() * 100
        drawdown = ((df["Close"].cummax() - df["Close"]) /
                    df["Close"].cummax()).max() * 100

        result.append({
            "symbol": symbol,
            "return_pct": round(returns, 2),
            "volatility": round(volatility, 2),
            "max_drawdown": round(drawdown, 2),
            "latest_price": round(end, 2)
        })

    return result
