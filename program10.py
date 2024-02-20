import requests
from bs4 import BeautifulSoup

url = "https://mycartshopping.000webhostapp.com/"
content = requests.get(url).content
# print(content)

soup = BeautifulSoup(content,'html.parser')

# find next siblings and previous siblings
element = soup.find('div').div
# print(element)
print(element.find_next_siblings())