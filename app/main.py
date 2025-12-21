from fastapi import FastAPI
from ingestion.load_data import load_metrics
from retrieval.evidence import collect_evidence
from retrieval.peers import peer_compare
from macro.rates import get_policy_rate
from app.reasoning import build_prompt
from app.llm import run_llm

app = FastAPI()
df = load_metrics()


@app.get("/ask")
def ask(bank: str, question: str):
    evidence = collect_evidence(bank, df)
    peers = peer_compare(bank, df)
    macro = get_policy_rate()

    prompt = build_prompt(bank, evidence, peers, macro)
    answer = run_llm(prompt)

    return {
        "bank": bank,
        "answer": answer
    }
