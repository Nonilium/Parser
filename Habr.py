import requests as rq
from bs4 import BeautifulSoup as bs


url = "https://habr.com/ru/articles/top/weekly/easy/"

response = rq.get(url)

soup = bs(response.text, "html.parser")

title = soup.findAll("a", class_="tm-title__link")

mas = []

for ti in title:
    title_words = ti.text

    with open(r"C:\Eagle\Parser\habr\Data_habr\title.txt", "r+") as f:
        mas.append(title_words)

        for i in mas:
            f.write(i)

for mas in mas:
    print(mas)
