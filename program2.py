import requests
from bs4 import BeautifulSoup

url = "https://mycartshopping.000webhostapp.com/"
content = requests.get(url).content
# print(content)

soup = BeautifulSoup(content,'html.parser')

# find method
print(soup.find("h1"))

image = soup.find("img")
print(image["src"])