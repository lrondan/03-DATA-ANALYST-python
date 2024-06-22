import requests
from bs4 import BeautifulSoup
import abrir_pagina

#pagina = webbrowser.open('index.html')
page = requests.get('https://es.wikipedia.org/wiki/Sistema_solar').text

#create bs object
soup = BeautifulSoup(page, 'html.parser')

#pull all instance of <table> tag
planets = soup.find_all('table')
results = []

for x in planets:
    results.append(str(x))

#write an file.txt
with open('index.html', 'w') as filew:
    for line in results:
        filew.write(line)