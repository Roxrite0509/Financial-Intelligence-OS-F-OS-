def bank_health_score(bank_data: dict):
    """
    Simple weighted score — evolve later
    """
    score = 0
    score += (20 - bank_data["npa"]) * 2
    score += bank_data["capital_adequacy"]
    score += (bank_data["deposits"] / bank_data["loans"]) * 10

    return round(score, 2)
