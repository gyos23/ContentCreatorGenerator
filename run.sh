#!/bin/bash

# Content Generator Launcher Script
# This script helps you run the app from anywhere

echo "🎬 Social Media Content Generator"
echo "=================================="
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Navigate to that directory
cd "$SCRIPT_DIR"

echo "📂 Running from: $SCRIPT_DIR"
echo ""
echo "Choose how to run:"
echo "  1. CLI Version (Terminal/Command Line)"
echo "  2. Web Version (Browser Interface)"
echo "  3. Exit"
echo ""
read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "🚀 Starting CLI version..."
        echo ""
        if command -v python3 &> /dev/null; then
            python3 content_generator.py
        elif command -v python &> /dev/null; then
            python content_generator.py
        else
            echo "❌ Error: Python is not installed"
            echo "Please install Python 3.7+ from https://www.python.org"
            exit 1
        fi
        ;;
    2)
        echo ""
        echo "🚀 Starting web server..."
        echo ""

        # Check if Flask is installed
        if python3 -c "import flask" 2>/dev/null; then
            echo "✅ Flask is installed"
        else
            echo "📦 Installing Flask..."
            pip3 install Flask flask-cors --quiet
        fi

        echo ""
        echo "🌐 Starting server at http://localhost:5000"
        echo "   Press Ctrl+C to stop"
        echo ""

        if command -v python3 &> /dev/null; then
            python3 api/index.py
        elif command -v python &> /dev/null; then
            python api/index.py
        else
            echo "❌ Error: Python is not installed"
            exit 1
        fi
        ;;
    3)
        echo "👋 Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac
