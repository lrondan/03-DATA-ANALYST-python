import requests
from bs4 import BeautifulSoup

#create request
page = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json').text

#beautifull soup object
soup = BeautifulSoup(page, 'html.parser')

#contenido
contenido = soup.get_text('')

#escribir archivo
with open('amd/amd.json', 'w')as json_file:
    for line in contenido:
        json_file.write(line)
print(type(contenido))