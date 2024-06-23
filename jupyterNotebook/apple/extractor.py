from bs4 import BeautifulSoup
import requests

page = requests.get('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json').text
soup = BeautifulSoup(page, 'html.parser')
linesw = soup.get_text('')

with open('apple.json','w') as json_file:
    for line in linesw:
        json_file.write(line)