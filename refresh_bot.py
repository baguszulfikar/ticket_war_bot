from bs4 import BeautifulSoup
import requests

page_url = input('masukan link konser tiket.com:')
# page = requests.get("https://www.tiket.com/to-do/arcticmonkeysjakarta?utm_page=toDoSearchResult")
page = requests.get(page_url)
soup = BeautifulSoup(page.content, 'html.parser')

# find a list of all span elements
pkg = soup.find_all('div', {'class' : 'package-card__header'})
div = soup.find_all('div', {'class' : 'pt__cta'})
title = soup.find('title')

cat = []
status = []
for i,j in enumerate(pkg):
    cat.append(j.contents[0].contents[0])

for i,j in enumerate(div):
    if j.contents[0].contents[0] != 'Pilih':
        status.append('HABIS')
    else:
        status.append('MASIH ADA')

full = {}

for key in cat:
    for value in status:
        full[key] = value
        status.remove(value)
        break

print(title.contents[0])
print(full)