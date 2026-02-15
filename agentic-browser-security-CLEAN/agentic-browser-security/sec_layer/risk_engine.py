def compute_risk(hidden_texts, dynamic_injections, phishing_findings):
    risk = 0
    reasons = []

    if hidden_texts:
        risk += 40
        reasons.append("Hidden instruction-like text detected")

    if dynamic_injections:
        risk += 30
        reasons.append("Dynamic DOM injection patterns detected")

    if phishing_findings:
        risk += 50
        reasons.append("Sensitive / phishing-like form detected")

    risk = min(risk, 100)
    return risk, reasons
