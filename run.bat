@echo off
REM Content Generator Launcher Script for Windows
REM This script helps you run the app from anywhere

echo.
echo 🎬 Social Media Content Generator
echo ==================================
echo.

REM Navigate to the directory where this script is located
cd /d "%~dp0"

echo 📂 Running from: %CD%
echo.
echo Choose how to run:
echo   1. CLI Version (Terminal/Command Line)
echo   2. Web Version (Browser Interface)
echo   3. Exit
echo.
set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo 🚀 Starting CLI version...
    echo.
    python content_generator.py
    if errorlevel 1 (
        python3 content_generator.py
    )
    if errorlevel 1 (
        echo ❌ Error: Python is not installed
        echo Please install Python 3.7+ from https://www.python.org
        pause
        exit /b 1
    )
) else if "%choice%"=="2" (
    echo.
    echo 🚀 Starting web server...
    echo.

    REM Check if Flask is installed
    python -c "import flask" 2>nul
    if errorlevel 1 (
        echo 📦 Installing Flask...
        pip install Flask flask-cors
    ) else (
        echo ✅ Flask is installed
    )

    echo.
    echo 🌐 Starting server at http://localhost:5000
    echo    Press Ctrl+C to stop
    echo.

    python api\index.py
    if errorlevel 1 (
        python3 api\index.py
    )
) else if "%choice%"=="3" (
    echo 👋 Goodbye!
    exit /b 0
) else (
    echo ❌ Invalid choice. Please run the script again.
    pause
    exit /b 1
)

pause
