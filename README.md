A proxyless parser for Google Maps written in pure python.

> Unlike Google Search, Google Maps doesn't seem to have endpoint limits, so this project was significantly more simple than my Google Search Parser.

## Requirements 

- Python 3.9+ with Python and PIP in your system PATH.
- 4GB+ DDR3 RAM or newer
- The latest version of Google Chrome.

# Usage

#### Note: Before running put your searches into queries.txt, one per line.

## Windows Usage

```powershell
# Navigating to the parser's dir.
cd /path/to/GMaps-Parser

# Installing required packages
pip install pyppeteer selenium webdriver_manager

# Running the scraper/parser combo script.
python main.py
```

## Linux / macOS Usage

```bash
# Navigating to the parser's dir.
cd /path/to/GMaps-Parser

# Creating a venv to isolate package installations
python3 -m venv ./

# Activating the venv
. bin/activate

# Installing required packages
pip3 install pyppeteer selenium webdriver_manager

# Running the scraper/parser combo script.
python3 main.py
```


