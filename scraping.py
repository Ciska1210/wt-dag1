print("Start scraping application")

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://en.bcmtoday.com/')
#print(pagina.content)

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
coinlist = heeldehtml.find('#coins-list')

print(coinlist.prettify())

spans = coinlist.find_all('span')
