def collect_evidence(bank, df):
    bank_df = df[df["bank"] == bank]

    return {
        "nim_trend": bank_df["nim"].tolist(),
        "gnpa_trend": bank_df["gnpa"].tolist(),
        "casa_trend": bank_df["casa"].tolist(),
        "capital": bank_df["capital"].iloc[-1]
    }
