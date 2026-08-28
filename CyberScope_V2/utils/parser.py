def parse_esp32_payload(payload):
    return {
        'sensor_id': payload.get('sensor_id', 'unknown'),
        'temperature': float(payload.get('temperature', 0.0)),
        'voltage': float(payload.get('voltage', 0.0)),
        'cpu_util': float(payload.get('cpu_util', 0.0)),
        'free_heap': float(payload.get('free_heap', 0.0)),
        'packet_drop': float(payload.get('packet_drop', 0.0)),
        'i2c_faults': int(payload.get('i2c_faults', 0)),
        'network_traffic': float(payload.get('network_traffic', 0.0)),
        'timestamp': payload.get('timestamp')
    }