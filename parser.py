# -*- coding: utf-8 -*-

import requests as rq
from bs4 import BeautifulSoup as bs


class Parser:
    def __init__(self):
        self.agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36"
        self.url = "https://www.archive.org"
        self.classes = ["desktop", "status-text", "hide-text", "cell-container", "block_container", "col"]
        self.id = ["item-size", "icon"]
        self.name = ["div", "span", "h4", "p", "a", "article", "col"]
        self.features = "html.parser"
        self.soup = bs(self.response().text, self.features)
        self.view = self.soup.findAll(name="div", class_=self.classes[0])

    def response(self):
        return rq.get(self.url)

    def text_page(self):
        return self.response().text

    def soup_page(self):
        return self.view


if __name__ == '__main__':

    p = Parser()

    status = p.response().status_code
    find = p.soup_page()

    if status == 200:
        print("Status Code:", status)

    print(find)
