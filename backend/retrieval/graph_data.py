import pandas as pd
import numpy as np

# backend/retrieval/graph_data.py


def stock_price_series(df, symbol: str):
    closes = df["Close"].tail(90)

    return {
        "symbol": symbol.upper(),
        "series": [
            {
                "date": str(idx.date()),
                "price": round(float(price), 2)
            }
            for idx, price in closes.items()
        ]
    }
