A proxy-less parser for Google Maps written in pure python.

## Workflow
- Enter your queries into `queries.txt` one per line.
- Enter the path to your chrome binary (if prompted).
- The scraper will make requests to `maps.google.com` using each query, then return all links found.
- The parser will return a `Business Name`, `Business Address`, `Business Phone`, `Business Website` for each link and pool this data into a CSV file.

> Unlike Google Search, Google Maps doesn't seem to have endpoint limits, so this project was significantly more simple than my Google Search Parser.

## Requirements 

- Python 3.9+ with Python and PIP in your system PATH.
- 4GB+ DDR3 RAM or newer
- The latest version of Google Chrome.

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


