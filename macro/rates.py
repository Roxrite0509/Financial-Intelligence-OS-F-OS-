import requests


def get_policy_rate():
    try:
        # Example public macro proxy
        r = requests.get("https://api.exchangerate.host/latest")
        return {
            "policy_rate": 6.5,  # mock RBI rate
            "confidence": 0.9
        }
    except:
        return {"policy_rate": None, "confidence": 0.0}
