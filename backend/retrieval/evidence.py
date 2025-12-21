from backend.market.prices import get_stock_price
from backend.macro.rates import get_policy_rate
from backend.ingestion.loaders import get_news


def build_evidence(country: str, bank_symbol: str, bank_name: str):
    return {
        "market": get_stock_price(bank_symbol),
        "policy": get_policy_rate(country),
        "news": get_news(bank_name)
    }
