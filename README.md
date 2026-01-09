# Selenium Pytest Mobile Emulator

This project uses **pytest** with **Selenium** for web UI testing on mobile emulators.

## Features

- Choose device via command line (`Pixel 7` or `iPhone SE`)
- `test_config` fixture to read `config.ini`

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

    pytest ./test/tests.test_opennet_hw --device "Pixel 7"
    pytest ./test/tests.test_opennet_hw --device "iPhone SE"

Default: `Pixel 7`.

### Test Demo - iPhone SE

<img src="./GIF/demo-ezgif.com-loop-count.gif" width="300" alt="Twitch Automation Test">
