import requests
from bs4 import BeautifulSoup

url = "https://mycartshopping.000webhostapp.com/"
content = requests.get(url).content
# print(content)

soup = BeautifulSoup(content,'html.parser')
elements = soup.find_all('h3')
element = elements[3]
# print(element)
previos_sibling = element.find_previous_sibling()
print(previos_sibling)

