# пример страницы
html = """<!DOCTYPE html>
<html lang="en">
<head>
<title>test page</title>
</head>
<body class="mybody" id="js-body">
<p class="text odd">first <b>bold</b> paragraph</p>
<p class="text even">second <a href="https://mail.ru">link</a></p>
<p class="list odd">third <a id="paragraph"><b>bold link</b></a></p>
</body>
</html>
"""
from bs4 import BeautifulSoup

# получаем код страницы
soup = BeautifulSoup(html, 'lxml')
# вывести код страницы
print("вывести код страницы")
print(soup)
# вывести крассивый код страницы
print("")
print("вывести крассивый код страницы")
print(soup.prettify())
# обратиться к первому тегу p
print("")
print("обратиться к первому тегу p")
x = soup.p
print(x)
print(type(x))
# обратиться к первому тегу b
print("")
print("обратиться к первому тегу b")
x = soup.b
print(x)
print(type(x))
# обратиться к первому тегу b внутри тега p
print("")
print("обратиться к первому тегу b внутри тега p")
x = soup.p.b
print(x)
print(type(x))
# обратиться к тексту внутри тега
print("")
print("обратиться к тексту внутри тега")
x = soup.p.b.string
print(x)
print(type(x))
# вывести имя тега
print("")
print("вывести имя тега")
x = soup.p.name
print(x)
# вывести список классов присвоенному этому тегу
print("")
print("вывести список классов присвоенному этому тегу")
x = soup.p['class']
print(x)
x = soup.body['id']
print(x)
# вывести родителя тега b
print("")
print("вывести родителя тега b")
x = soup.p.b.parent
print(x)
# вывести всех родителей тега b ЭТО БУДЕТ ГЕНЕРАТОР
print("")
print("вывести всех родителей тега b ЭТО БУДЕТ ГЕНЕРАТОР")
x = soup.p.b.parents
print(x)
print("Разбор генератора")
x = [tag.name for tag in soup.p.b.parents]
print(x)
# следующий после тега
print("")
print("следующий после тега")
x = soup.p.next
print(x)
x = soup.p.next.next
print(x)
# следующий тег, исключая вложенные. Но может быть перевод строки
print("")
print("следующий тег, исключая вложенные")
x = soup.p.next_sibling
print(x)
x = soup.p.next_sibling.next_sibling
print(x)
# получить все вложенные теги
print("")
print("получить все вложенные теги")
x = soup.p.contents
print(x)
# получить генератор вложенных тегов
x = soup.p.children
print(x)
print(list(x))
