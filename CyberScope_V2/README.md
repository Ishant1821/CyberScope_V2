# CyberScope-AI (v2.0): Multi-Dimensional IoT Security Information & Event Management (SIEM)

CyberScope-AI is an advanced, lightweight, machine-learning-powered SIEM platform engineered specifically for monitoring resource-constrained IoT edge networks (such as ESP32 microcontrollers). Version 2.0 introduces a robust **7-Dimensional telemetry ingestion engine**, unsupervised anomaly detection via `scikit-learn`, and a fully overhauled, glassmorphism-styled Security Operations Center (SOC) dashboard.

---

## 🚀 Key Upgrades in Version 2.0

*   **7-Dimensional Feature Space:** Expands beyond basic hardware monitoring to simultaneously correlate **Temperature, Voltage, CPU Utilization (%), Free Heap Memory (KB), Packet Drop Rate (%), I2C Bus Faults, and Network Traffic Volume (KB/s)**.
*   **Unsupervised Machine Learning Core:** Utilizes an optimized **Isolation Forest** ensemble model to establish baseline behavioral norms and detect zero-day cyber threats (such as DDoS botnet floods and memory exhaustion/buffer overflows) without static threshold limitations.
*   **Multi-Tiered Threat Visualization:** Features dedicated, split-stream charts built with `Chart.js` tracking real-time network volatility and processing loads, alongside a dynamic 3-way traffic distribution matrix (Normal, Warning, Critical).
*   **Intelligent Forensic Threat Heuristics:** Automatically correlates cross-metric spikes to generate descriptive incident insights (e.g., detecting simultaneous CPU saturation and network flooding).
*   **Enterprise Security & Compliance:** Secured via `Flask-Login` session management, password hashing (`Werkzeug`), CLI-based administrative provisioning, and an automated ReportLab PDF compliance report generator.

---

## 📊 System Architecture & Metrics

| Metric Category | Parameters Tracked | Primary Threat Vector Addressed |
| :--- | :--- | :--- |
| **Hardware Health** | Temperature (°C), Voltage (V) | Thermal overloads, Power supply surges, Short circuits |
| **System Load** | CPU Utilization (%), Free Heap (KB) | Crypto-mining malware, Resource exhaustion, Buffer overflows |
| **Network Integrity**| Traffic Volume (KB/s), Packet Drop (%) | DDoS botnet floods, Data exfiltration, Network jamming |
| **Bus / Peripheral** | I2C Read Errors / Faults | Physical tampering, Sensor disconnects |

---

## 🛠️ Technology Stack

*   **Backend & API:** Python 3, Flask, Flask-Login, SQLite3, Werkzeug, python-dotenv
*   **Machine Learning:** scikit-learn, NumPy, Joblib, SciPy metrics (Precision, Recall, F1-Score)
*   **Frontend UI:** HTML5, CSS3 (Glassmorphism & Multi-Theme Profiles), JavaScript, Chart.js
*   **Testing & Tooling:** Pytest, ReportLab (PDF Engine), Batch Automation Scripts

---

## ⚙️ Quick Start & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ishant1821/CyberScope_V2.git](https://github.com/Ishant1821/CyberScope_V2.git)
   cd CyberScope_V2