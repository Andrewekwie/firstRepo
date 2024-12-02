import requests
from bs4 import BeautifulSoup
import time
# response = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
# print(response.content)
# soup = BeautifulSoup(response.text, features="html.parser")
# BTC = soup.find("span", {"class": "sc-65e7f566-0 WXGwg base-text"})
# print(BTC.text)

response = requests.get("https://coinmarketcap.com/")
soup = BeautifulSoup(response.text, features="html.parser")
while True:

    coins = [soup.find_all('p',  {'class':"sc-65e7f566-0 iPbTJf coin-item-name"}),
            soup.find_all('p',  {'class':"sc-65e7f566-0 byYAWx coin-item-symbol"}),
            soup.find_all( 'div', {'class':"sc-b3fc6b7-0 dzgUIj"})

            ]
    file = open("coins.txt", "w")
    for i in range(0,len(coins[0])):
        print(f"{coins[0][i].text} {coins[1][i].text} {coins[2][i].text}")
        file.write(f"{coins[0][i].text} {coins[1][i].text} {coins[2][i].text}\n")
    file.close()
    time.sleep(5)

