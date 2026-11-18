# Lab 33: Basic Web Scraping with requests and BeautifulSoup

## Objective

Learn how to retrieve webpage content using Python's `requests` library and extract information from HTML using BeautifulSoup.

## Tools and Libraries

- Python 3
- requests 2.32.3
- beautifulsoup4 4.12.3
- Ubuntu Linux
- HTML

## Concepts Learned

### 1. HTTP GET Request

The `requests.get()` function sends an HTTP GET request to a website and retrieves its response.

```python
response = requests.get(url, timeout=10)
```

### 2. HTTP Status Code

The status code tells us whether the request was successful.

- `200`: Request successful.
- `404`: Page not found.
- `500`: Server error.

### 3. Error Handling

`raise_for_status()` raises an exception if the HTTP response contains an unsuccessful status code.

```python
response.raise_for_status()
```

### 4. HTML Parsing

BeautifulSoup parses HTML and makes it easier to extract information.

```python
soup = BeautifulSoup(response.text, 'html.parser')
```

### 5. Prettify HTML

The `prettify()` method displays parsed HTML in a readable, structured format.

```python
print(soup.prettify())
```

### 6. Extract Page Title

The page title can be accessed using:

```python
title = soup.title.string
print("Page Title:", title)
```

### 7. Extract Hyperlinks

The `find_all('a')` method finds all anchor tags. The `get('href')` method retrieves each link.

```python
links = soup.find_all('a')

for link in links:
    print(link.get('href'))
```

## Practical Implementation

The `scrape.py` script:

1. Accepts a website URL as a command-line argument.
2. Sends an HTTP GET request with a 10-second timeout.
3. Checks the HTTP response.
4. Parses the HTML using BeautifulSoup.
5. Displays formatted HTML.
6. Extracts the page title.
7. Finds and prints hyperlinks.

## How to Run

Install the required packages:

```bash
pip install requests beautifulsoup4
```

Run the scraper:

```bash
python scrape.py https://example.com
```

For the local HTML test:

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

Open another terminal and run:

```bash
python scrape.py http://127.0.0.1:8000/
```

Another website used for hyperlink extraction:

```bash
python scrape.py https://www.python.org
```

## Testing and Verification

- Both local and external HTTP requests returned status code `200`.
- Local webpage title was successfully extracted: `Local Test Page`.
- All three local test hyperlinks were extracted.
- Python.org hyperlinks were successfully extracted.
- Python syntax check passed using `python -m py_compile scrape.py`.

**Testing note:** The example.com response in this lab environment did not contain an anchor element. Python.org was used as an additional real-website test to verify hyperlink extraction.

## Evidence

The `evidence/` directory contains:

- Package versions
- Local server status
- HTTP fetch status codes
- Parsed HTML output
- Extracted local title and hyperlinks
- Python.org extracted hyperlinks
- Verification results
- Full Python.org scraper output

## Important Notes

- Always use a request timeout.
- Check HTTP responses before processing them.
- Keep SSL certificate verification enabled.
- Respect website terms, robots.txt rules, and reasonable request rates when scraping websites.

## Result

Successfully completed the practical implementation of basic web scraping using Python `requests` and BeautifulSoup.

**LMS Result: 100 / 100 — Passed**
