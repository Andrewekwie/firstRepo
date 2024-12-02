import requests
from bs4 import BeautifulSoup
import time
# response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
# print(response.content)
# soup = BeautifulSoup(response.text, features="html.parser")
# BTC = soup.find("span", {"class": "sc-65e7f566-0 WXGwg base-text"})
# print(BTC.text)


response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")
books = [soup.find_all('h3'),
         soup.find_all('p',{"class":"price_color"})


         ]

for i in range(0,len(books[0])):
     print(f"{books[0][i].text} {books[1][i].text}")


