import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.quotegarden.com/mind.html")
soup = BeautifulSoup(response.text, features="html.parser")
txt = soup.find('p',{"align":"left"})

print(txt.text)

