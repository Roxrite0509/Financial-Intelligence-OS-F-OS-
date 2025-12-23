# backend/analysis/metrics.py
import numpy as np


def compute_metrics(df):
    closes = df["Close"]

    returns = closes.pct_change().dropna()

    return {
        "price": round(float(closes.iloc[-1]), 2),
        "return_pct": round(float((closes.iloc[-1] / closes.iloc[0] - 1) * 100), 2),
        "volatility": round(float(np.std(returns) * 100), 2),
    }
