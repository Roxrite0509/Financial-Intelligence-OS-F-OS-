from datetime import datetime, timedelta


def freshness(timestamp):
    ts = datetime.fromisoformat(timestamp)
    delta = datetime.utcnow() - ts

    if delta < timedelta(hours=1):
        return "LIVE"
    if delta < timedelta(days=1):
        return "RECENT"
    return "STALE"
