from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

from ingestion.stocks import get_stock_history
from retrieval.graph_data import stock_price_series
from analysis.comparisons import compare_banks
from analysis.ai import explain_stock_move
from analysis.metrics import compute_metrics

app = FastAPI(title="F-OS India Bank Intelligence")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Stock Snapshot
# -----------------------------


@app.get("/market/stock")
def market_stock(symbol: str = Query(...)):
    df = get_stock_history(symbol)
    if df is None:
        return {"error": "No market data found"}

    metrics = compute_metrics(df)
    return {
        "symbol": symbol.upper(),
        **metrics
    }

# -----------------------------
# Price Graph
# -----------------------------


@app.get("/market/graph")
def market_graph(symbol: str = Query(...)):
    df = get_stock_history(symbol)
    if df is None:
        return {"error": "No data"}

    return stock_price_series(df, symbol)

# -----------------------------
# Bank Comparison
# -----------------------------


@app.get("/market/compare")
def market_compare(symbols: str = Query(...)):
    results = []

    for s in symbols.split(","):
        df = get_stock_history(s.strip())
        if df is None:
            continue

        metrics = compute_metrics(df)
        results.append({
            "symbol": s.strip().upper(),
            **metrics
        })

    return compare_banks(results)

# -----------------------------
# AI Insight
# -----------------------------


@app.get("/market/ai")
def market_ai(symbol: str = Query(...)):
    df = get_stock_history(symbol)
    if df is None:
        return {"error": "No market data"}

    metrics = compute_metrics(df)

    insight = explain_stock_move(
        symbol.upper(),
        metrics["return_pct"],
        metrics["volatility"]
    )

    return {
        "symbol": symbol.upper(),
        "insight": insight
    }
