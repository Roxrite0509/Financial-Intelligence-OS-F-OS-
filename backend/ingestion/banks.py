BANKS = {
    "HDFCBANK": {
        "loans": 2300000,
        "deposits": 2100000,
        "npa": 1.3,
        "capital_adequacy": 18.5
    },
    "ICICIBANK": {
        "loans": 1900000,
        "deposits": 1800000,
        "npa": 1.1,
        "capital_adequacy": 17.2
    }
}


def get_bank_snapshot(bank: str):
    return BANKS.get(bank.upper())
