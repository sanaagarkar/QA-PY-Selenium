# QA-PY-Selenium-Simple-Usage

A Python-based Selenium automation project designed to demonstrate simple usage of Selenium for web testing. This project includes examples of unit tests, Pytest integration, and HTML test report generation.

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Generating Reports](#generating-reports)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- Automates browser interactions using Selenium.
- Supports unit testing with Python's `unittest` module.
- Integrates with `pytest` for advanced testing.
- Generates HTML test reports for better visualization of test results.

---

## Prerequisites
Before running this project, ensure you have the following installed:
- Python 3.6 or later
- A compatible WebDriver (e.g., ChromeDriver, GeckoDriver)
- A modern web browser (e.g., Chrome, Firefox)

---

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sanaagarkar/QA-PY-Selenium.git
   cd QA-PY-Selenium
   ```

2. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Download the appropriate WebDriver for your browser:
   - ChromeDriver
   - GeckoDriver

4. Add the WebDriver to your system's PATH or specify its location in the code.

---

## Usage
To run the project, follow these steps:

### Running Individual Scripts
Run a specific script using:
```sh
python3 <script_name>.py
```

### Running Unit Tests
Run the unittest tests:
```sh
python3 -m unittest discover
```

### Running Pytest Tests
Run the pytest tests:
```sh
pytest pytest_tests.py
```

---

## Project Structure
```markdown
qa-py-selenium-simple-usage/
├── reports/                     # HTML test reports
├── simple_tests.py              # Basic Selenium test example
├── unittest_tests.py            # Unit tests using unittest
├── pytest_tests.py              # Tests using pytest
├── html_testRunner_reports_tests.py # Tests with HTML report generation
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## Running Tests
To run all tests, use the following command:
```sh
pytest
```

---

## Generating Reports
To generate HTML test reports, use the following command:
```sh
pytest --html=reports/report.html
```

---

## Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:
git checkout -b feature/your-feature-name

Commit your changes:
git commit -m "Add your message here

Push to your branch:

git push origin feature/your-feature-name 
---

Contact
For any questions or feedback, feel free to reach out:

Author: Sana Agarkar
GitHub: sanaagarkar
```
