# CyberScope-AI (v2.0): Multi-Dimensional IoT Security Information & Event Management (SIEM)

CyberScope-AI is an advanced, lightweight, machine-learning-powered SIEM platform engineered specifically for monitoring resource-constrained IoT edge networks (such as ESP32 microcontrollers). Version 2.0 introduces a robust **7-Dimensional telemetry ingestion engine**, unsupervised anomaly detection via `scikit-learn` (utilizing a standardized preprocessing pipeline), and a fully overhauled, glassmorphism-styled Security Operations Center (SOC) dashboard.

## Key Upgrades in Version 2.0
* **7-Dimensional Feature Space:** Expands beyond basic hardware monitoring to simultaneously correlate **Temperature (C), Voltage (V), CPU Utilization (%), Free Heap Memory (KB), Packet Drop Rate (%), I2C Bus Faults, and Network Traffic Volume (KB/s)**.
* **Optimized Unsupervised Machine Learning Core:** Utilizes an optimized **Isolation Forest** ensemble model wrapped in a `StandardScaler` feature pipeline, achieving a high precision score of **81.04%** and reducing false alarms to 117 while retaining 100.0% recall on evaluated attack scenarios[cite: 6].
* **Dynamic Tech Stack & Persistence:** Implements SQLAlchemy ORM with native dual support for transactional **SQLite** (default for lightweight edge and local reproducibility) and **PostgreSQL** (for scalable enterprise SOC deployments)[cite: 6].
* **Multi-Tiered Threat Visualization:** Features dedicated, split-stream charts built with `Chart.js` tracking real-time network volatility and processing loads, alongside a dynamic 3-way traffic distribution matrix (Normal, Warning, Critical)[cite: 6].
* **Intelligent Forensic Threat Heuristics:** Automatically correlates cross-metric spikes to generate descriptive incident insights (e.g., detecting simultaneous CPU saturation and network flooding)[cite: 6].
* **Enterprise Security & Compliance:** Secured via `Flask-Login` session management, password hashing (`Werkzeug`), CLI-based administrative provisioning, and an automated ReportLab PDF compliance report generator[cite: 6].

## System Architecture & Metrics
| Metric Category | Parameters Tracked | Primary Threat Vector Addressed |[cite: 6] |
| :--- | :--- | :--- | :--- |
| **Hardware Health** | Temperature (C), Voltage (V) | Thermal overloads, Power supply surges, Short circuits[cite: 6] |
| **System Load** | CPU Utilization (%), Free Heap (KB) | Crypto-mining malware, Resource exhaustion, Buffer overflows[cite: 6] |
| **Network Integrity**| Traffic Volume (KB/s), Packet Drop (%) | DDoS botnet floods, Data exfiltration, Network jamming[cite: 6] |
| **Bus / Peripheral** | I2C Read Errors / Faults | Physical tampering, Sensor disconnects[cite: 6] |

## Technology Stack
* **Backend & API:** Python 3, Flask, Flask-Login, Flask-SQLAlchemy, SQLite3 / PostgreSQL, Werkzeug, python-dotenv[cite: 6]
* **Machine Learning:** scikit-learn (Isolation Forest, StandardScaler Pipeline), NumPy, Joblib, SciPy metrics[cite: 6]
* **Frontend UI:** HTML5, CSS3 (Glassmorphism & Multi-Theme Profiles), JavaScript, Chart.js[cite: 6]
* **Testing & Tooling:** Pytest, ReportLab (PDF Engine), Batch Automation Scripts (`start_cyberscope.bat`)[cite: 6]

## Quick Start & Installation
1. **Clone the repository:**[cite: 6]
   ```bash
   git clone [https://github.com/Ishant1821/CyberScope_V2.git](https://github.com/Ishant1821/CyberScope_V2.git)
   cd CyberScope_V2
