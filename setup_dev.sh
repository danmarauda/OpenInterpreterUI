#!/bin/bash

echo "Setting up OpenInterpreterUI with development branch..."

# Create and activate virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Uninstall existing open-interpreter if present
echo "Removing existing open-interpreter installation..."
pip uninstall -y open-interpreter

# Install requirements with development branch
echo "Installing requirements with development branch..."
pip install -r requirements.txt

# Run test script
echo "Running test script..."
python test_interpreter.py

echo "Setup complete! Please check the test results above."