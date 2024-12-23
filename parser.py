# -*- coding: utf-8 -*-
import requests as rq
# from ascii import file_ascii as file
from bs4 import BeautifulSoup as bs


class Parser:
    def __init__(self):
        self.agent = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/51.0.2704.103 Safari/537.36")
        self.url = ("https://www.archive.org/" + str("details/booksbylanguage_indonesian?tab=collection"))
        self.classes = ["status-text", "hide-text", "cell-container", "block_container", "col"]
        self.id = ["item-size", "icon"]
        self.name = ["div", "span", "h4", "p", "a", "article", "col"]
        self.features = "html.parser"
        self.soup = bs(self.response().text, self.features)
        self.block_container = self.soup.find(class_=" grid ")
        self.view = self.soup.find(name="li", class_="icon")

    def response(self):
        return rq.get(self.url)

    def check_view(self):
        return self.soup

    def title(self):
        return self.block_container()

    def status(self):
        return self.view()


if __name__ == '__main__':

    p = Parser()

    status = p.response().status_code
    title = p.title()

    if status == 200:
        print("Status Code:", status)

    print(title)
