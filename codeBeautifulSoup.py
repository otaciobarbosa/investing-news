import requests
from bs4 import BeautifulSoup
#from html.parser import HTMLParser

headers = {
    'authority': 'br.investing.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-gpc': '1',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
}

response = requests.get('https://br.investing.com/news/latest-news', headers=headers)
html = BeautifulSoup(response.content, 'html.parser')
divs = html.find_all("div", {"class":'largeTitle'})
article = []
for x in divs:
  article = x.find_all("article")


for x in article:
  print(x)