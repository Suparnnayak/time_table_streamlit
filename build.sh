#!/bin/bash
# Build script for Render deployment
# This ensures we use the correct Python version and install dependencies

set -e

echo "Setting up Python environment..."

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Build completed successfully!"

