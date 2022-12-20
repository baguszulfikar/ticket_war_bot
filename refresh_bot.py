from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.tiket.com/to-do/arcticmonkeysjakarta?utm_page=toDoSearchResult")
soup = BeautifulSoup(page.content, 'html.parser')

# find a list of all span elements
pkg = soup.find_all('div', {'class' : 'package-card__header'})
div = soup.find_all('div', {'class' : 'pt__cta'})
# h5 = div.find_all('h5')
# for i,j in enumerate(pkg[0:3]):
    # if i.contents[0] == 'CAT 1':
    # print(j.contents[0].contents[0])
for i,j in enumerate(div[0:3]):
    print(j.contents[0].contents[0])