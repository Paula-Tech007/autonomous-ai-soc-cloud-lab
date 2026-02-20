# 🛡️ Autonomous AI SOC Lab (Cloud + Docker)

## Overview
A modular Cloud Security + DevSecOps + AI Automation lab integrating:
- Threat Intelligence (simulated/API)
- CVE Monitor
- Phishing Detection
- Risk Score Engine
- Streamlit Dashboard
- Docker & Docker Compose
- Cloud Deploy (Render/AWS)

## Project Structure
```
ai-soc-cloud-lab/
│
├── app/
│   ├── app.py
│   ├── risk_engine.py
│   ├── threat_intel.py
│   ├── cve_monitor.py
│   ├── phishing_detector.py
│   ├── data_simulator.py
│
├── data/
│   └── sample_events.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## MVP Features
- Event simulator
- Risk engine
- Functional dashboard
- Local Docker container

## Run Locally
1. Build and start container:
   ```
docker compose up --build
```
2. Access dashboard:
   - http://localhost:8501

## Next Steps
- Integrate real APIs
- Cloud deployment
