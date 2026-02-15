def enforce_policy(risk):
    if risk >= 60:
        return "BLOCK"
    elif risk >= 30:
        return "WARN"
    else:
        return "ALLOW"
