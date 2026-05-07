# Sporty Group QA Automation Assignment

## Overview

This project contains automated test coverage for the Sporty Group QA assignment.

Implemented automation includes:
- UI E2E test for successful bet placement
- API validation test for maximum stake business rule

The framework was intentionally kept lightweight and maintainable to focus on readability, stability, and clear project structure.

---

## Tech Stack

- Python 3
- Pytest
- Selenium WebDriver
- Requests
- WebDriver Manager
- Google Chrome

---

## Project Structure

```text
automation/
├── README.md
├── conftest.py
├── requirements.txt
├── pages/
│   └── bet_page.py
├── tests/
│   ├── api/
│   │   └── test_place_bet_api_validation.py
│   └── ui/
│       └── test_single_bet_placement.py
└── utils/
    └── config.py
```

---

## Setup

Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run UI Test

```bash
pytest tests/ui/test_single_bet_placement.py -v -s
```

---

## Run API Test

```bash
pytest tests/api/test_place_bet_api_validation.py -v -s
```

---

## Notes

- `webdriver-manager` is used to automatically manage compatible ChromeDriver versions.
- Explicit waits were used to improve UI test stability and reduce flaky behavior.
- Console step logs were intentionally added to improve execution readability during assignment review.