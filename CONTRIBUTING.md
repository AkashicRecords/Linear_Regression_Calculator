# Contributing to Linear Regression Calculator

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## How to Contribute

1. Fork the repository:
   - Visit https://github.com/AkashicRecords/Linear_Regression_Calculator
   - Click the "Fork" button in the top right

2. Clone your fork:
```bash
git clone https://github.com/YOUR_USERNAME/Linear_Regression_Calculator.git
cd Linear_Regression_Calculator
```

3. Set up your development environment:
```bash
# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

4. Create a new branch:
```bash
git checkout -b feature/YourFeatureName
# or
git checkout -b bugfix/YourBugfixName
```

5. Make your changes:
   - Add or modify code
   - Add tests if applicable
   - Update documentation if needed

6. Run tests locally before committing:
```bash
# Run all tests
python -m pytest tests/

# Run a specific test file
python -m pytest tests/test_linear_regression.py

# Run a specific test function
python -m pytest tests/test_linear_regression.py::test_linear_regression_fit

# Run tests with verbose output
python -m pytest -v tests/

# Check code style
flake8 .
```

7. Commit your changes:
```bash
git add .
git commit -m "Description of your changes"
```

8. Push to your fork:
```bash
git push origin feature/YourFeatureName
```

9. Create a Pull Request:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Click "Create Pull Request"
   - Add a title and description of your changes

## Pull Request Guidelines

- Update the README.md with details of changes if needed
- Update the documentation with details of any changes to the interface
- The PR should work for Python 3.6+
- Make sure your code follows the existing style
- Include comments in your code where necessary
- Ensure all tests pass locally before submitting the PR

## Running Tests

Before submitting your PR, make sure all tests pass:

1. Install test dependencies:
```bash
pip install pytest flake8
```

2. Run the test suite:
```bash
# Run all tests
python -m pytest tests/

# Run with coverage report
python -m pytest --cov=. tests/
```

3. Check code style:
```bash
# Check for syntax errors and undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

# Check for style issues (warnings only)
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

Common test commands:
- `pytest -v`: Run tests with verbose output
- `pytest -k "test_name"`: Run tests matching "test_name"
- `pytest --pdb`: Drop into debugger on test failures
- `pytest --cov=. --cov-report=html`: Generate HTML coverage report

## Development Process

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Run tests locally to ensure everything works
4. Ensure the code follows our style guidelines
5. Issue that pull request!

## Any Questions?

- Feel free to open an issue with your question
- Tag it with "question" for faster response

## License

By contributing, you agree that your contributions will be licensed under the MIT License. 