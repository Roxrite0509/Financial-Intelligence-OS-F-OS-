from datetime import datetime


def get_policy_rate(country: str):
    rates = {
        "India": 6.5,
        "USA": 5.25,
        "UK": 5.25
    }

    return {
        "policy_rate": rates.get(country, None),
        "timestamp": datetime.utcnow().isoformat(),
        "source": "Central Bank (fallback)",
        "confidence": 0.7
    }
