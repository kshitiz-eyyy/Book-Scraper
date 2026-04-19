import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

all_books = []

for page in range(1, 4):  # scrape first 3 pages
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text

        rating_class = book.find("p", class_="star-rating")["class"]
        rating = rating_class[1]  # e.g., "Three"

        all_books.append([title, price, rating])

# Save to CSV
with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Rating"])
    writer.writerows(all_books)

print("Scraping completed. Data saved to books.csv")