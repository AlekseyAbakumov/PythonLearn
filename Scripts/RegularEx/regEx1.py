import re

text = "Карта map и объект bitmap - это разные вещи"

# найти все вхождения
match = re.findall(r"map", text)
print(match)
# найти вхождения, где слово является самостоятельным словом
match = re.findall(r"\bmap\b", text)
print(match)

# символьные классы
text = "Еда, беду, победа"
match = re.findall(r"[еЕ]д[ау]", text)
print(match)
text = "Еда, беду, 5 победа"
match = re.findall(r"[123456789]", text)
match = re.findall(r"[1-9]", text)
print(match)
text = "Еда, беду, 55 победа"
match = re.findall(r"[123456789]", text)
print(match)
text = "Еда, беду, 5 55 победа"
match = re.findall(r"[123456789][1-9]", text)
print(match)
# найти не цифры
text = "Еда, беду, 5 55 победа."
match = re.findall(r"[^0-9]", text)
print(match)
# не русские маленькие буквы
text = "Еда, беду, 5 55 победа."
match = re.findall(r"[^а-я]", text)
print(match)
# не русские маленькие или БОЛЬШИЕ буквы
text = "Еда, беду, 5 55 победа."
match = re.findall(r"[^а-яА-Я]", text)
print(match)
# не русские маленькие или БОЛЬШИЕ буквы и не цифры
text = "Еда, беду, 5 55 победа."
match = re.findall(r"[^а-яА-Я0-9]", text)
print(match)
# не русские маленькие или БОЛЬШИЕ буквы и не цифры и не запятая
text = "Еда, беду, 5 55 победа."
match = re.findall(r"[^,а-яА-Я0-9]", text)
print(match)

# краткие записи символьных классов
# найти только цифры
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\d", text)
print(match)
# найти не цифры
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\D", text)
print(match)
# любой пробел, табуляция, возврат каретки, перевод строки и т.д.
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\s", text)
print(match)
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\S", text)
print(match)
# любой символ слова, цифры. Знаки препинания не включаются
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\w", text)
print(match)
text = "Еда, беду, 5 55 победа."
match = re.findall(r"\W", text)
print(match)

# убрать все русские символы
text = "Еда, беду, 5 55 победа. Hello World"
match = re.findall(r"\w", text, re.ASCII)
print(match)
