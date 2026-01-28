#!/bin/bash

echo "Flask Application Test Runner"
echo "=============================="
echo ""

# Check if Flask is installed
if ! python3 -c "import flask" &> /dev/null; then
    echo "Error: Flask is not installed"
    echo "Please run: pip3 install -r requirements.txt"
    exit 1
fi

echo "Running unit tests..."
echo ""
python3 test_app.py

if [ $? -eq 0 ]; then
    echo ""
    echo "=============================="
    echo "All tests passed successfully!"
    echo "=============================="
else
    echo ""
    echo "=============================="
    echo "Some tests failed!"
    echo "=============================="
    exit 1
fi
