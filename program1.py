# importing necessary modules
import requests
from bs4 import BeautifulSoup

# defining the url for scraping the web
url = "https://mycartshopping.000webhostapp.com/"
# accessing content from website as plain string
content = requests.get(url).content
# print(content)

# parsing the html content
soup = BeautifulSoup(content,'html.parser')

# accessing a sample data
print(soup.h1.text)