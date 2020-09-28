html = """
<!DOCTYPE html>
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
soup=BeautifulSoup(html,'lxml')
# найти родителя b у которого есть id js-body
print("найти родителя b у которого есть id js-body")
x=soup.p.b.find_parent(id="js-body").name
print(x)

# найти следующий тег и отфильтровать его по нужному параметру
print("")
print("найти следующий тег и отфильтровать его по нужному параметру")
x=soup.p.find_next_sibling(class_="odd")
print(x)

# изменить тег
print("")
print("изменить тег")
tag=soup.b
print(tag)

tag.name="i"
tag['id']="myid"
tag.string='italic'
tag=soup.b
print(tag)