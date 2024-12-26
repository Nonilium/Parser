import time
import requests as rq
from bs4 import BeautifulSoup as bs

start = time.time()

for i in range(1, 10**5 + 1):
    url = f"https://habr.com/ru/articles/{i}/"

    response = rq.get(url)

    soup = bs(response.text, "html.parser")

    title = soup.findAll(name="h1", class_="tm-title tm-title_h1")

    page = soup.findAll(name="span", class_="tm-pagination__page tm-pagination__page_current")

    mas = []

    for ti in title:
        title_words = ti.text
        with open(r"C:\Eagle\Parser\habr\Data_habr\title.txt", "w", encoding="utf-8") as f:
            mas.append(title_words)

            f.write(title_words)

            for m in mas:
                print(m)


end = time.time()

print(end - start)