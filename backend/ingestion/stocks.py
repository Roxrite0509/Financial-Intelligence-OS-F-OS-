import yfinance as yf

SYMBOL_MAP = {
    "SBI": "SBIN.NS",
    "HDFC": "HDFCBANK.NS",
    "ICICI": "ICICIBANK.NS"
}


def normalize_symbol(symbol: str) -> str:
    symbol = symbol.upper().strip()
    return SYMBOL_MAP.get(symbol, symbol)


def get_stock_history(symbol: str):
    symbol = normalize_symbol(symbol)

    ticker = yf.Ticker(symbol)

    for period, interval in [
        ("1mo", "1d"),
        ("6mo", "1d"),
        ("1y", "1d"),
    ]:
        try:
            df = ticker.history(period=period, interval=interval)
            if not df.empty:
                df.reset_index(inplace=True)
                return df
        except Exception:
            continue

    return None


def get_stock_history(symbol: str):
    symbol = symbol.upper()
    if not symbol.endswith(".NS"):
        symbol = symbol + ".NS"

    ticker = yf.Ticker(symbol)
    df = ticker.history(period="6mo")

    if df.empty:
        return None

    return df
