from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.retrieval.evidence import build_evidence
from backend.app.reasoning import generate_insights
from fastapi import FastAPI
from backend.market.prices import router as market_router

app = FastAPI()

app.include_router(market_router)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/dashboard")
def dashboard(country: str, bank_symbol: str, bank_name: str):
    evidence = build_evidence(country, bank_symbol, bank_name)
    insights = generate_insights(evidence)
    return {
        "data": evidence,
        "insights": insights
    }
