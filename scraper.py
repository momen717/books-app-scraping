import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
OUTPUT_FILE = "books.csv"


def get_rating(rating_class):
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)


def scrape_books():
    books = []

    for page_number in range(1, 6):
        page_url = urljoin(BASE_URL, f"catalogue/page-{page_number}.html")

        response = requests.get(page_url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        book_elements = soup.select("article.product_pod")

        for book in book_elements:
            title = book.h3.a["title"]

            price_text = book.select_one(".price_color").text.strip()
            print("PRICE:", repr(price_text))

            price = float(price_text.replace("Â£", "").strip())

            rating_class = book.select_one(".star-rating")["class"][1]
            rating = get_rating(rating_class)

            stock_text = book.select_one(".availability").get_text(" ", strip=True)
            in_stock = "In stock" in stock_text

            relative_url = book.h3.a["href"]
            book_url = urljoin(page_url, relative_url)

            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "in_stock": in_stock,
                "url": book_url
            })

    return books


def save_to_csv(books):
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["title", "price", "rating", "in_stock", "url"]
        )

        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    books = scrape_books()
    save_to_csv(books)

    print(f"Successfully scraped {len(books)} books.")
    print(f"Saved to {OUTPUT_FILE}")