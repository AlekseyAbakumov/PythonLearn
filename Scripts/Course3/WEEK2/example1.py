import requests
from bs4 import BeautifulSoup

# получить с указанного сайта список ссылок
resp = requests.get("https://wikipedia.org")
html = resp.text

# ссылки указаны внутри тега <a> класса class="other-project-link"
# сами ссылки находятся в атрибуте href
soup = BeautifulSoup(html, 'lxml')
tags = soup('a', 'other-project-link')
# помещаем в генератор списков
x = [tag['href'] for tag in tags]
print(x)
