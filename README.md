# mapit

Open any location in Google Maps from the command line, plus a few Python practice scripts on regex, Excel files and web scraping.

## mapit

| Script | What it does |
| --- | --- |
| `mapit.py` | Asks for a location and opens it in Google Maps. |
| `mapitsys.py` | Takes the location from command-line arguments. With no arguments, it offers to use the address on your clipboard or asks you to type one. |

### Usage

```bash
pip install pyperclip

python mapit.py
python mapitsys.py Statue of Unity, Gujarat
python mapitsys.py          # uses clipboard or asks for input
```

## Practice scripts

### `patternmatching/`
- `pattern1.py`: finds phone numbers in text with `re`.
- `pattern2.py`: demonstrates regex character classes such as `\d`, `\w` and `\s`.

### `webscraping/`
- `requestslearn.py`: downloads a web page with `requests` and saves it to a file.
- `soup1.py`: scrapes book titles from [books.toscrape.com](https://books.toscrape.com) with BeautifulSoup.
- `webbrowserlearn.py`: opens a Google search in the browser.
- `create_xl.py`, `read_xl.py`, `openpyxl_learn.py`: create and read Excel files with `openpyxl`.
- `pythonvers.py`: prints which Python interpreter is running.
- `statueofunity.txt`: a saved sample page used for scraping practice.

## Requirements

Python 3 and:

```bash
pip install pyperclip requests beautifulsoup4 openpyxl
```
