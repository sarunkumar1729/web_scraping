import requests
from bs4 import BeautifulSoup

url = "https://mycartshopping.000webhostapp.com/"
content = requests.get(url).content
# print(content)

soup = BeautifulSoup(content,'html.parser')
print(soup.select('div.grid-item'))