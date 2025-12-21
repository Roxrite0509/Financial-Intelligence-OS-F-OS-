def detect_trend(values):
    if len(values) < 2:
        return "UNKNOWN"

    if values[-1] > values[-2]:
        return "RISING"
    if values[-1] < values[-2]:
        return "FALLING"
    return "FLAT"
