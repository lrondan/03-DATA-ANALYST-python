import requests
from bs4 import BeautifulSoup
import webbrowser


pagina = webbrowser.open('index.html')
page = requests.get('file:///C:/Users/ALEX/Desktop/03%20DATA%20ANALYST%20python/web%20scraping/index.html').text

#create bs object
soup = BeautifulSoup(page, 'html5lib')

#pull all instance of <tr> tag
artist = soup.find_all('tr')

#clear data all tags
for artist in artist:
    name = artist.contents[0]
    fullLink=artist.get('href')
    print(name)
    print(fullLink)