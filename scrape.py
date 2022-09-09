import requests
from bs4 import BeautifulSoup
import csv
from datetime import date
   
URL = "https://www.theverge.com/"
r = requests.get(URL)
   
soup = BeautifulSoup(r.content, 'html5lib')

articles=[] 
count = 0
   
main = soup.find('main', attrs = {'id':'content'}) 

for row in main.findAll('div', attrs = {'class':'c-entry-box--compact__body'}):
    if row.find('time'):
        article = {}
        article['id'] = count
        article['url'] = row.h2.a['href']
        article['headline'] = row.h2.text
        article['author'] = row.find('span', attrs = {'class':'c-byline__author-name'}).text
        article['date'] = row.time['datetime'].split("T")[0]
        articles.append(article)
        count += 1

# print(articles)

today = date.today()
d1 = today.strftime("%d%m%Y")
filename = f'{d1}_verge.csv'

with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['id','url','headline','author','date'])
    w.writeheader()
    for article in articles:
        w.writerow(article)