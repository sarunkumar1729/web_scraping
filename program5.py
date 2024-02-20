# finding by class name
import requests
from bs4 import BeautifulSoup

url = "https://mycartshopping.000webhostapp.com/"
content = requests.get(url).content
# print(content)

soup = BeautifulSoup(content,'html.parser')
items = soup.find_all(class_='grid-item')


for item in items:
      print(item.h3.text)
      print(item.p.text)