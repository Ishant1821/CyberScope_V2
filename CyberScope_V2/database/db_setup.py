import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'cyberscope.db')

def init_db(admin_user=None, admin_pass=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS incidents
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  sensor_id TEXT,
                  temperature REAL,
                  voltage REAL,
                  cpu_util REAL,
                  free_heap REAL,
                  packet_drop REAL,
                  i2c_faults INTEGER,
                  network_traffic REAL,
                  timestamp TEXT,
                  classification TEXT)''')
                  
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL
                )''')
                
    if admin_user and admin_pass:
        hashed_pw = generate_password_hash(admin_pass)
        c.execute("""
            INSERT INTO users (username, password_hash) 
            VALUES (?, ?) 
            ON CONFLICT(username) DO UPDATE SET password_hash=excluded.password_hash
        """, (admin_user, hashed_pw))
    else:
        c.execute("SELECT * FROM users WHERE username='admin'")
        if not c.fetchone():
            hashed_pw = generate_password_hash('admin123')
            c.execute("INSERT INTO users (username, password_hash) VALUES ('admin', ?)", (hashed_pw,))
        
    conn.commit()
    conn.close()

def log_incident(sensor_id, temp, volt, cpu, heap, drop, faults, traffic, timestamp, classification):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""INSERT INTO incidents 
                 (sensor_id, temperature, voltage, cpu_util, free_heap, packet_drop, i2c_faults, network_traffic, timestamp, classification) 
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
              (sensor_id, temp, volt, cpu, heap, drop, faults, traffic, timestamp, classification))
    conn.commit()
    conn.close()

def get_incidents():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM incidents")
    rows = c.fetchall()
    conn.close()
    return rows

def clear_incidents():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('DELETE FROM incidents')
    c.execute('DELETE FROM sqlite_sequence WHERE name="incidents"')
    conn.commit()
    conn.close()

def get_user_by_username(username):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user