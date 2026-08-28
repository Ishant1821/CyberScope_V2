import time
import random
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))
URL = "http://localhost:5000/api/ingest"
API_KEY = os.environ.get('CYBERSCOPE_API_KEY', 'esp32_secure_key_2026')

def generate_data():
    if random.random() > 0.85:
        # Simulate active cyber attack / hardware failure
        temp = random.uniform(70.0, 100.0)
        voltage = random.uniform(4.5, 6.0)
        cpu_util = random.uniform(85.0, 99.9)        # CPU pegged
        free_heap = random.uniform(10.0, 50.0)       # Memory exhausted
        packet_drop = random.uniform(15.0, 40.0)     # Network congestion
        i2c_faults = random.randint(5, 20)           # Hardware faults
        network_traffic = random.uniform(500.0, 2000.0) # Data exfiltration/DDoS flood
    else:
        # Normal operational baselines
        temp = random.uniform(25.0, 35.0)
        voltage = random.uniform(3.1, 3.5)
        cpu_util = random.uniform(10.0, 30.0)
        free_heap = random.uniform(200.0, 280.0)
        packet_drop = random.uniform(0.0, 1.0)
        i2c_faults = 0
        network_traffic = random.uniform(10.0, 50.0)
        
    return {
        "sensor_id": "ESP32-01",
        "temperature": round(temp, 2),
        "voltage": round(voltage, 2),
        "cpu_util": round(cpu_util, 2),
        "free_heap": round(free_heap, 2),
        "packet_drop": round(packet_drop, 2),
        "i2c_faults": i2c_faults,
        "network_traffic": round(network_traffic, 2),
        "timestamp": datetime.datetime.now().isoformat()
    }

def run_sim():
    print("Starting ESP32 7D Simulator... Press Ctrl+C to stop.")
    headers = {
        "Content-Type": "application/json",
        "X-API-Key": API_KEY
    }
    
    while True:
        data = generate_data()
        try:
            response = requests.post(URL, json=data, headers=headers)
            if response.status_code == 401:
                print("CRITICAL ERROR: Unauthorized! Check your API key.")
                break
            print(f"Sent: Temp={data['temperature']}C, CPU={data['cpu_util']}%, Net={data['network_traffic']}KB/s | Status: {response.status_code}")
        except Exception as e:
            print(f"Connection failed. Is the Flask app running?")
            
        time.sleep(2)

if __name__ == "__main__":
    run_sim()