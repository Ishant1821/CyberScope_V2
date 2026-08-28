# CyberScope-AI (v2.0) — Multi-Dimensional IoT SIEM Platform

CyberScope-AI is a lightweight, machine-learning-powered Security Information and Event Management (SIEM) system built to monitor resource-constrained IoT edge devices (such as ESP32 microcontrollers). Version 2.0 scales the platform into a robust **7-Dimensional telemetry analysis engine**, capable of unsupervised anomaly detection, real-time threat visualization, and automated compliance reporting.

---

## 📸 Platform Preview & UI Overhaul

### 1. SOC Monitoring Overview Dashboard
*The primary glassmorphism interface displaying real-time system integrity clusters, 3-way traffic distribution, and isolated network/CPU trendlines.*
![Dashboard Overview]("Assets CS_V2/dashboard.png")

### 2. Multi-Model Performance Comparison
*Benchmark analysis evaluating the Isolation Forest model against alternative algorithms across high-dimensional telemetry matrices.*
![Model Comparison]("Assets CS_V2/comparision.png")

### 3. Incident Management Ledger
*The historical tracking and compliance log featuring color-coded threat severity tiers and instant CSV/PDF export options.*
![Incident Ledger]("Assets CS_V2/incidents.png")

### 4. Advanced Log Analyzer
*Dedicated tool for parsing and auditing batch log files against the unsupervised anomaly detection engine.*
![Log Analyzer]("Assets CS_V2/loganalyser.png")

---

## 🚀 Key Features & Capabilities

*   **7-Dimensional Telemetry Ingestion:** Simultaneously tracks and processes **Temperature (°C), Voltage (V), CPU Utilization (%), Free Heap Memory (KB), Packet Drop Rate (%), I2C Bus Faults, and Network Traffic Volume (KB/s)**.
*   **Unsupervised Machine Learning Core:** Employs an optimized **Isolation Forest** anomaly detection model trained on multi-variable baseline distributions to flag zero-day attacks (e.g., DDoS floods, memory exhaustion, buffer overflows) without manual threshold configuration.
*   **Intelligent Forensic Heuristics:** Cross-references metrics at the edge to generate contextual, human-readable threat insights (e.g., identifying synchronized CPU spikes and network traffic surges as potential botnet/DDoS activity).
*   **Enterprise-Grade Security:** Includes session management via `Flask-Login`, secure password hashing (`Werkzeug`), CLI credential provisioning, and automated PDF compliance reporting via `ReportLab`.

---

## 📊 System Architecture & Metrics

| Metric Category | Parameters Monitored | Primary Threat Vector Addressed |
| :--- | :--- | :--- |
| **Hardware Health** | Temperature, Voltage | Thermal overloads, Power fluctuations, Short circuits |
| **System Load** | CPU Utilization, Free Heap Memory | Resource exhaustion, Cryptojacking, Memory leaks |
| **Network Integrity** | Traffic Volume, Packet Drop Rate | DDoS floods, Network jamming, Data exfiltration |
| **Bus / Peripheral** | I2C Bus Faults / Read Errors | Physical sensor tampering, Hardware disconnects |

---

## 🛠️ Technology Stack

*   **Backend & API:** Python 3, Flask, Flask-Login, SQLite3, Werkzeug, python-dotenv
*   **Machine Learning:** scikit-learn, NumPy, Joblib, SciPy (Precision, Recall, F1 metrics)
*   **Frontend UI:** HTML5, CSS3 (Glassmorphism & Multi-Theme Profiles), JavaScript, Chart.js
*   **Testing & Tooling:** Pytest, ReportLab (PDF Engine), Automated Windows Launch Scripts

---

## ⚙️ Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ishant1821/CyberScope_V2.git](https://github.com/Ishant1821/CyberScope_V2.git)
   cd CyberScope_V2