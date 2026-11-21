@echo off
cd /d "%~dp0"
py -3 --version >nul 2>&1
if not errorlevel 1 (
    py -3 run_web.py
) else (
    python run_web.py
)
pause
