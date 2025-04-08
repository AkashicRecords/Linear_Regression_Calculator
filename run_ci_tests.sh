#!/bin/bash

# Exit on error
set -e

echo "Running CI tests locally..."

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
pip install pytest pytest-cov numpy matplotlib
if [ -f requirements.txt ]; then 
    pip install -r requirements.txt
fi

# Run tests with coverage
echo "Running tests with coverage..."
pytest --cov=./ --cov-report=xml --cov-report=term-missing

# Generate coverage report
echo "Generating coverage report..."
echo "## Test Coverage Report"
echo "### Overall Coverage"
coverage report --format=markdown

echo "### Failed Tests"
pytest tests/ -v --cov=. --cov-report=term-missing 2>&1 | grep -A 10 "FAILED" || true

echo "### Coverage Details"
echo "```"
coverage report
echo "```"

# Check if tests passed
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    exit 0
else
    echo "❌ Some tests failed. Please fix them before pushing."
    exit 1
fi 