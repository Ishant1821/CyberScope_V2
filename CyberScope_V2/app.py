from flask import Flask, request, jsonify, render_template, redirect, url_for, send_file
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from utils.parser import parse_esp32_payload
from utils.detector import detect_anomaly
from utils.pdf_generator import generate_incident_pdf
from database.db_setup import init_db, log_incident, get_incidents, clear_incidents, get_user_by_username, get_user_by_id
import datetime
import csv
import io
import json
import os
import argparse
import getpass
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')
app.config['API_KEY'] = os.environ.get('CYBERSCOPE_API_KEY', 'default_api_key')

init_db()
total_logs_processed = 0

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    user_record = get_user_by_id(user_id)
    if user_record:
        return User(id=user_record[0], username=user_record[1])
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_record = get_user_by_username(username)
        
        if user_record and check_password_hash(user_record[2], password):
            user = User(id=user_record[0], username=user_record[1])
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid credentials. Access denied.'
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def dashboard():
    incidents = get_incidents()
    total_anomalies = len(incidents)
    return render_template('dashboard.html', incidents=incidents, total_anomalies=total_anomalies, total_logs=total_logs_processed, active_page='dashboard')

@app.route('/incidents')
@login_required
def incidents_view():
    incidents = get_incidents()
    return render_template('incidents.html', incidents=incidents, active_page='incidents')

@app.route('/analytics')
@login_required
def analytics_view():
    benchmark_data = {}
    if os.path.exists('benchmark_results.json'):
        with open('benchmark_results.json', 'r') as f:
            benchmark_data = json.load(f)
    return render_template('analytics.html', active_page='analytics', benchmark_data=benchmark_data)

@app.route('/analyzer', methods=['GET', 'POST'])
@login_required
def analyzer_view():
    scan_results = []
    error_message = None
    if request.method == 'POST':
        file = request.files.get('log_file')
        if file:
            stream = io.StringIO(file.stream.read().decode("UTF-8"), newline=None)
            csv_reader = csv.DictReader(stream)
            headers = csv_reader.fieldnames
            
            if not headers:
                error_message = "The uploaded file is empty or unreadable."
            else:
                for row in csv_reader:
                    try:
                        # Safely parse old and new formats, defaulting new metrics to safe baselines
                        payload = {
                            'temperature': float(row.get('temperature', row.get('temp', 0.0))),
                            'voltage': float(row.get('voltage', row.get('volt', 0.0))),
                            'cpu_util': float(row.get('cpu_util', 20.0)),
                            'free_heap': float(row.get('free_heap', 240.0)),
                            'packet_drop': float(row.get('packet_drop', 0.0)),
                            'i2c_faults': int(row.get('i2c_faults', 0)),
                            'network_traffic': float(row.get('network_traffic', 30.0))
                        }
                        is_anomaly, reason = detect_anomaly(payload)
                        scan_results.append({
                            'temperature': payload['temperature'],
                            'voltage': payload['voltage'],
                            'is_anomaly': is_anomaly,
                            'reason': reason
                        })
                    except (ValueError, KeyError):
                        continue
    return render_template('analyzer.html', scan_results=scan_results, active_page='analyzer', error_message=error_message)

@app.route('/export/pdf')
@login_required
def export_pdf():
    incidents = get_incidents()
    buffer = io.BytesIO()
    generate_incident_pdf(incidents, buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='cyberscope_compliance_report.pdf', mimetype='application/pdf')

@app.route('/api/ingest', methods=['POST'])
def ingest_data():
    api_key = request.headers.get('X-API-Key')
    if api_key != app.config['API_KEY']:
        return jsonify({"status": "error", "message": "Unauthorized device"}), 401
        
    global total_logs_processed
    payload = request.json
    if not payload:
        return jsonify({"status": "error", "message": "No JSON payload"}), 400
        
    total_logs_processed += 1
    parsed_data = parse_esp32_payload(payload)
    is_anomaly, reason = detect_anomaly(parsed_data)
    
    if is_anomaly:
        log_incident(
            parsed_data['sensor_id'],
            parsed_data['temperature'],
            parsed_data['voltage'],
            parsed_data['cpu_util'],
            parsed_data['free_heap'],
            parsed_data['packet_drop'],
            parsed_data['i2c_faults'],
            parsed_data['network_traffic'],
            parsed_data.get('timestamp', datetime.datetime.now().isoformat()),
            reason
        )
        return jsonify({"status": "anomaly_logged"}), 201
    return jsonify({"status": "ok"}), 200

@app.route('/api/reset', methods=['POST'])
@login_required
def reset_data():
    global total_logs_processed
    total_logs_processed = 0
    clear_incidents()
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="CyberScope-AI SOC Server")
    parser.add_argument('--username', type=str, help="Admin username")
    parser.add_argument('--password', type=str, help="Admin password")
    args = parser.parse_args()

    admin_user = args.username or input("Enter SOC Admin Username: ")
    admin_pass = args.password or getpass.getpass("Enter SOC Admin Password: ")

    init_db(admin_user=admin_user, admin_pass=admin_pass)
    print(f"\n[+] CyberScope-AI initialized with active admin user: {admin_user}\n")
    app.run(debug=True, port=5000)