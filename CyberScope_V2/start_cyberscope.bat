@echo off
title CyberScope-AI Launcher
color 0B
echo ===================================================
echo      CyberScope-AI SOC Platform Initialization
echo ===================================================
echo.

set /p ADMIN_USER="Enter SOC Admin Username: "
set /p ADMIN_PASS="Enter SOC Admin Password: "

echo.
echo [1/4] Running ML Benchmark to update analytics data...
python benchmark.py
echo.
echo [2/4] Starting the Flask SIEM Server...
start "CyberScope-AI Server" cmd /k "python app.py --username %ADMIN_USER% --password %ADMIN_PASS%"

echo [3/4] Starting the ESP32 IoT Edge Simulator...
start "ESP32 Simulator" cmd /k "python sim/mock_esp32.py"

echo [4/4] Launching the SOC Dashboard...
timeout /t 3 /nobreak > NUL
start http://127.0.0.1:5000

echo.
echo ===================================================
echo SUCCESS: All systems are online!
echo You can close this launcher window safely.
echo ===================================================
pause