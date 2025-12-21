def peer_compare(bank, df):
    peers = df[df["bank"] != bank]

    peer_avg = peers.groupby("bank").mean(numeric_only=True).mean()

    return {
        "peer_avg_nim": round(peer_avg["nim"], 2),
        "peer_avg_gnpa": round(peer_avg["gnpa"], 2),
        "peer_avg_casa": round(peer_avg["casa"], 2)
    }
