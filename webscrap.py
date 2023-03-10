import os
import requests
from bs4 import BeautifulSoup
class WebScraper:
    def __init__(self, domain, span, tag):
        self.domain = domain
        self.span = span
        self.tag = tag

    def get_data(self):
        url = 'https://' + self.domain + self.span
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find(self.tag).text
        return data

domain = input("Masukkan domain: ")
if domain:
    span = input("Masukkan span: ")
    if len(span)<=100:
        tag = input("Masukkan tag yang ingin di scrap: ")
        scraper = WebScraper(domain, span, tag)
        data = scraper.get_data()
        print(data)
    else:
        print("Span terlalu panjang, maksimum 100 karakter")
else:
    print("Domain tidak boleh kosong")
