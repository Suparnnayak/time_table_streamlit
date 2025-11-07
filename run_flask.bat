@echo off
echo ========================================
echo Educational Chatbot - Flask Server
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

echo [2/3] Checking dependencies...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo Dependencies are installed.
)
echo.

echo [3/3] Starting Flask server...
echo.
echo ========================================
echo Server will start on: http://localhost:5000
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause

