import random

def generate_event():
    event_types = ["phishing", "cve", "threat"]
    event_type = random.choice(event_types)
    if event_type == "phishing":
        return {
            "type": "phishing",
            "email": "fake@malicious.com"
        }
    if event_type == "cve":
        return {
            "type": "cve",
            "cve_id": "CVE-2025-1234",
            "severity": random.randint(1, 10)
        }
    if event_type == "threat":
        return {
            "type": "threat",
            "ip": "192.168.1.100",
            "intel_score": random.randint(10, 100)
        }
