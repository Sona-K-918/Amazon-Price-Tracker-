# Amazon Price Tracker

A Python-based Amazon Price Tracker that monitors Amazon product prices and stores price history in a CSV file. The application uses Selenium and BeautifulSoup to extract product information directly from Amazon pages and provides a simple GUI built with CustomTkinter.

---

## Features

- Track Amazon product prices using a product URL
- Extract product title and current price
- Compare current price with previously stored price
- Detect:
  - Price Dropped 🔥
  - Price Increased 📈
  - Price Unchanged ➖
- Store price history in a CSV file
- Modern GUI using CustomTkinter
- Automated browser interaction using Selenium

---

## Project Structure

```text
Amazon-Price-Tracker/
│
├── assets/
│   ├── amazon_smile.png
│   └── background.png
│
├── app.py
├── tracker.py
├── ui.py
├── prices.csv
├── requirements.txt
├── README.md
│
└── Docs/
    └── Screenshots/
```

---

## Libraries Used

### Selenium

Used for browser automation.

Purpose:
- Opens Amazon product pages automatically
- Loads dynamic content that may not be available through a simple HTTP request
- Provides page source for scraping

Import:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
```

---

### WebDriver Manager

Used to automatically download and manage the correct ChromeDriver version.

Purpose:
- Eliminates manual ChromeDriver installation
- Keeps driver version compatible with Chrome browser

Import:

```python
from webdriver_manager.chrome import ChromeDriverManager
```

---

### BeautifulSoup

Used for HTML parsing and data extraction.

Purpose:
- Extract product title
- Extract current product price
- Parse the page source returned by Selenium

Import:

```python
from bs4 import BeautifulSoup
```

---

### Pandas

Used for data storage and analysis.

Purpose:
- Read previous prices from CSV
- Store current prices in CSV
- Compare historical and current prices

Import:

```python
import pandas as pd
```

---

### CustomTkinter

Used for the graphical user interface.

Purpose:
- Create modern UI components
- URL input field
- Track button
- Results display box
- Custom styling

Import:

```python
import customtkinter as ctk
```

---

### Pillow (PIL)

Used for image handling.

Purpose:
- Load background image
- Load Amazon logo image
- Display images inside GUI

Import:

```python
from PIL import Image
```

---

### Time

Used for delays during browser loading.

Purpose:
- Allow Amazon page to load completely before scraping

Import:

```python
import time
```

---

## Workflow

1. User enters an Amazon product URL.
2. Selenium opens the product page.
3. BeautifulSoup extracts product title and price.
4. Pandas reads previous price history.
5. Current price is compared with the last recorded price.
6. Status is generated:
   - Price Dropped 🔥
   - Price Increased 📈
   - Price Unchanged ➖
7. Latest price is saved to `prices.csv`.
8. Results are displayed in the GUI.

---

## Installation

Install required packages:

```bash
pip install selenium
pip install beautifulsoup4
pip install pandas
pip install webdriver-manager
pip install customtkinter
pip install pillow
```

Or:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Launch the GUI:

```bash
python ui.py
```

---

## Future Improvements

- Email notifications for price drops
- Multiple product tracking
- Price trend graphs
- Scheduled automatic tracking
- Database integration
- Export reports

---

## Author

Sonakshi Kaushik
