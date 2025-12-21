import yfinance as yf
from datetime import datetime
from fastapi import APIRouter

router = APIRouter()


def get_stock_price(symbol: str):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")

    if data.empty:
        return {"error": "No data"}

    latest = data.iloc[-1]

    return {
        "symbol": symbol,
        "price": round(float(latest["Close"]), 2),
        "change": round(float(latest["Close"] - latest["Open"]), 2),
        "timestamp": datetime.utcnow().isoformat()
    }


@router.get("/market/price")
def market_price(symbol: str):
    return get_stock_price(symbol)
