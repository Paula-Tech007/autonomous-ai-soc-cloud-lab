import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Autonomous AI SOC Lab", layout="wide")

st.title("🛡️ Autonomous AI SOC Cloud Lab")

# -----------------------------
# SESSION STATE
# -----------------------------
if "events" not in st.session_state:
    st.session_state.events = []

# -----------------------------
# EVENT SIMULATOR
# -----------------------------
def generate_event():
    event_type = random.choice(["cve", "phishing", "brute_force", "malware"])
    severity = random.randint(1, 10)

    return {
        "timestamp": datetime.now(),
        "type": event_type,
        "severity": severity
    }

# -----------------------------
# RISK ENGINE
# -----------------------------
def calculate_risk(event):
    base_score = event["severity"] * 10

    if event["type"] == "malware":
        base_score += 20
    elif event["type"] == "brute_force":
        base_score += 10
    elif event["type"] == "phishing":
        base_score += 5

    return min(base_score, 100)

def classify_risk(score):
    if score < 30:
        return "LOW"
    elif score < 60:
        return "MEDIUM"
    elif score < 80:
        return "HIGH"
    else:
        return "CRITICAL"

# -----------------------------
# CONTROLS
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    if st.button("Simulate Security Event"):
        event = generate_event()
        risk_score = calculate_risk(event)
        event["risk_score"] = risk_score
        event["risk_level"] = classify_risk(risk_score)
        st.session_state.events.append(event)

with col2:
    auto_mode = st.checkbox("Enable Auto Mode (Real-Time Simulation)")

# -----------------------------
# RESET BUTTON
# -----------------------------
if st.button("Reset SOC Environment"):
    st.session_state.events = []
    st.rerun()

# -----------------------------
# AUTO MODE
# -----------------------------
if auto_mode:
    event = generate_event()
    risk_score = calculate_risk(event)
    event["risk_score"] = risk_score
    event["risk_level"] = classify_risk(risk_score)
    st.session_state.events.append(event)
    time.sleep(2)
    st.rerun()

# -----------------------------
# DISPLAY LAST EVENT
# -----------------------------

# -----------------------------
# SOC METRICS (KPIs)
# -----------------------------
st.subheader("SOC Metrics")
total_events = len(st.session_state.events)
if total_events > 0:
    avg_risk = sum(e["risk_score"] for e in st.session_state.events) / total_events
else:
    avg_risk = 0
col1_kpi, col2_kpi = st.columns(2)
col1_kpi.metric("Total Events", total_events)
col2_kpi.metric("Average Risk Score", round(avg_risk, 2))

# -----------------------------
# DISPLAY LAST EVENT
# -----------------------------
if st.session_state.events:
    last_event = st.session_state.events[-1]

    st.subheader("Latest Event")
    st.json({
        "timestamp": str(last_event["timestamp"]),
        "type": last_event["type"],
        "severity": last_event["severity"],
        "risk_score": last_event["risk_score"],
        "risk_level": last_event["risk_level"]
    })

    st.subheader("Risk Assessment")

    if last_event["risk_level"] == "LOW":
        st.success(f"Risk Level: {last_event['risk_level']}")
    elif last_event["risk_level"] == "MEDIUM":
        st.warning(f"Risk Level: {last_event['risk_level']}")
    else:
        st.error(f"Risk Level: {last_event['risk_level']}")

    st.metric("Risk Score", last_event["risk_score"])

# -----------------------------
# HISTORICAL GRAPH
# -----------------------------
if st.session_state.events:
    st.subheader("Risk Trend Over Time")

    df = pd.DataFrame(st.session_state.events)
    df = df.set_index("timestamp")

    st.line_chart(df["risk_score"])