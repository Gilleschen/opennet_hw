# Selenium Pytest Mobile Emulator

This project uses **pytest** with **Selenium** for web UI testing on mobile emulators.

## Features

- Use pytest as the testing framework
- Support centralized configuration (config.ini)
- Share test initialization and fixtures (conftest.py)
- Separate element locators from test logic (locator.py)

## Project Structure

```
.
├── libs/
│   └── __init__.py
│   └── actions.py
├── tests/
│   └── __init__.py
│   └── test_opennet_hw.py
├── GIF/
├── screenshot/
├── config.ini
├── locator.py
├── conftest.py
├── requirements.txt
└── README.md
```

## Test Data Setup

Set the test data in `config.ini` :

```
[Twitch]
TwitchURL = https://www.twitch.tv
GameName = StarCraft II
```

## Install

    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    pip install -r requirements.txt

Requirements:

    pytest
    selenium

## Usage

### Run Pytest

    pytest ./test/tests.test_opennet_hw

### Choose Device

Support Pixel 7 and iPhone SE

    pytest ./test/tests.test_opennet_hw --device "Pixel 7"
    pytest ./test/tests.test_opennet_hw --device "iPhone SE"

Default: `Pixel 7`

### Test Demo

<img src="./GIF/demo-ezgif.com-loop-count.gif" width="300" alt="Twitch Automation Test">
