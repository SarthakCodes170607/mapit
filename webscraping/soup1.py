import requests
from bs4 import BeautifulSoup

# Step 1: Download the page
url = "https://books.toscrape.com"   # a free practice scraping website!
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
response.raise_for_status()

# Step 2: Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract what you need
# On books.toscrape.com, book titles are in <h3> tags inside <article>
books = soup.find_all("article", class_="product_pod")

print(f"Found {len(books)} books\n")

for book in books[:5]:   # first 5 books
    title = book.find("h3").find("a")["title"]
    price = book.find("p", class_="price_color").getText()
    print(f"📖 {title} — {price}")