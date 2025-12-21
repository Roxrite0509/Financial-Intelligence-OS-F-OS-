def build_prompt(bank, evidence, peers, macro):
    return f"""
You are a banking analyst.

Bank: {bank}

Bank metrics:
- NIM trend: {evidence['nim_trend']}
- GNPA trend: {evidence['gnpa_trend']}
- CASA trend: {evidence['casa_trend']}
- Capital adequacy: {evidence['capital']}

Peer averages:
- Peer NIM: {peers['peer_avg_nim']}
- Peer GNPA: {peers['peer_avg_gnpa']}
- Peer CASA: {peers['peer_avg_casa']}

Macro:
- Policy rate: {macro['policy_rate']}

Answer:
1. Is the bank more or less vulnerable than peers?
2. Key risks
3. One-line conclusion
"""
