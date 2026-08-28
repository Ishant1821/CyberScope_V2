import pytest
import json
import sys
import os

# Ensure the tests can find your main app files
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
from utils.detector import detect_anomaly

@pytest.fixture
def client():
    """Sets up a mock Flask server for testing the API."""
    app.config['TESTING'] = True
    app.config['API_KEY'] = 'test_secure_key'
    with app.test_client() as client:
        yield client

# --- 1. Machine Learning 7D Logic Tests ---
def test_ml_detector_normal():
    """Test that the 7D ML model correctly identifies safe operational baselines."""
    payload = {
        'temperature': 30.5,
        'voltage': 3.3,
        'cpu_util': 20.0,
        'free_heap': 240.0,
        'packet_drop': 0.1,
        'i2c_faults': 0,
        'network_traffic': 25.0
    }
    is_anomaly, reason = detect_anomaly(payload)
    
    # Assert that safe operations do NOT trigger an anomaly
    assert is_anomaly is False
    assert reason == "Normal"

def test_ml_detector_extreme_anomaly():
    """Test that the 7D ML model catches severe coordinated botnet/DDoS spikes."""
    payload = {
        'temperature': 95.0,
        'voltage': 5.5,
        'cpu_util': 98.5,
        'free_heap': 15.0,
        'packet_drop': 35.0,
        'i2c_faults': 12,
        'network_traffic': 1500.0
    }
    is_anomaly, reason = detect_anomaly(payload)
    
    # Assert that the multi-dimensional threat is caught and flagged
    assert is_anomaly is True
    assert "CRITICAL" in reason

# --- 2. REST API Endpoint Tests ---
def test_api_ingest_normal(client):
    """Test that the server accepts normal 7D API telemetry and returns HTTP 200 (OK)."""
    payload = {
        "sensor_id": "TEST-ESP32",
        "temperature": 29.5,
        "voltage": 3.29,
        "cpu_util": 18.5,
        "free_heap": 250.0,
        "packet_drop": 0.0,
        "i2c_faults": 0,
        "network_traffic": 30.0
    }
    headers = {"X-API-Key": app.config['API_KEY']}
    response = client.post('/api/ingest', json=payload, headers=headers)
    
    assert response.status_code == 200
    assert response.get_json()['status'] == 'ok'

def test_api_ingest_anomaly_logging(client):
    """Test that the server correctly logs 7D anomalies to the database and returns HTTP 201 (Created)."""
    payload = {
        "sensor_id": "TEST-ESP32",
        "temperature": 92.0,
        "voltage": 5.8,
        "cpu_util": 92.0,
        "free_heap": 20.0,
        "packet_drop": 25.0,
        "i2c_faults": 8,
        "network_traffic": 1200.0
    }
    headers = {"X-API-Key": app.config['API_KEY']}
    response = client.post('/api/ingest', json=payload, headers=headers)
    
    assert response.status_code == 201
    assert response.get_json()['status'] == 'anomaly_logged'