def calculate_risk(event):
    score = 0
    if event["type"] == "phishing":
        score += 30
    if event["type"] == "cve":
        score += event.get("severity", 5) * 5
    if event["type"] == "threat":
        score += event.get("intel_score", 50) / 2
    if score < 30:
        level = "LOW"
    elif score < 60:
        level = "MEDIUM"
    elif score < 90:
        level = "HIGH"
    else:
        level = "CRITICAL"
    return score, level
