import joblib
import os
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/anomaly_model.pkl')

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

def generate_insight(data):
    """Generates a human-readable threat report based on multi-dimensional telemetry context."""
    temp = data['temperature']
    volt = data['voltage']
    cpu = data['cpu_util']
    heap = data['free_heap']
    faults = data['i2c_faults']
    traffic = data['network_traffic']

    # Cross-reference metrics to deduce the cyber threat
    if cpu > 85.0 and traffic > 500.0:
        return f"CRITICAL: CPU ({cpu}%) and Network Traffic ({traffic} KB/s) spiked simultaneously. Probable botnet/DDoS hijack."
    elif heap < 50.0 and cpu > 85.0:
        return f"CRITICAL: Resource exhaustion. Heap critical ({heap} KB). Potential buffer overflow or malicious process."
    elif faults > 5:
        return f"WARNING: High I2C bus read errors ({faults}). Suspected physical tampering or sensor disconnect."
    elif temp > 90 and volt > 5.0:
        return f"CRITICAL: Simultaneous thermal ({temp} C) and power ({volt}V) surge. High risk of hardware short-circuit."
    elif temp > 90:
        return f"WARNING: Thermal anomaly ({temp} C) detected independently of network load. Check external heat sources."
        
    return "Minor multi-dimensional variance detected. Operating parameters drifting outside established baselines."

def detect_anomaly(data):
    # Fallback heuristic rules
    if model is None:
        if data['temperature'] > 80 or data['voltage'] > 5.0 or data['cpu_util'] > 90 or data['network_traffic'] > 500:
            return True, generate_insight(data)
        return False, "Normal"
        
    # Shape the 7D array exactly as it was trained
    features = np.array([[
        data['temperature'], data['voltage'], data['cpu_util'], 
        data['free_heap'], data['packet_drop'], data['i2c_faults'], data['network_traffic']
    ]])
    
    prediction = model.predict(features)
    
    if prediction[0] == -1:
        insight = generate_insight(data)
        return True, insight
        
    return False, "Normal"