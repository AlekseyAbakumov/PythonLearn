# квантификаторы

import re

text = "Google, Gooogle, Gooooooogle"
# символ может повторяться от 2 до 7 раз
# мажорный режим. Старается найти МАКСИМАЛЬНУЮ длинну
match = re.findall(r"o{2,7}", text)
print(match)
# минорный режим. Старается найти МИНИМАЛЬНУЮ длинну
match = re.findall(r"o{2,7}?", text)
print(match)

text = "Google, Gooogle, Gooooooogle"
# буква o может идти от двух и более раз
# мажорный режим.
match = re.findall(r"Go{2,}gle", text)
print(match)
# буква o может идти не более четырех раз
# мажорный режим.
match = re.findall(r"Go{,4}gle", text)
print(match)

# проверка номера телефона. Сначала должна идти 8, затем 10 цифр
phone="89163634627"
phone2="79163634627"
phone3="8913654"
match=re.findall(r"8\d{10}", phone)
match2=re.findall(r"8\d{10}", phone2)
match3=re.findall(r"8\d{10}", phone3)
print(match, match2, match3)

# хотим найти оба слова. Т.е. вторая буква н может быть, а может и нет
text="стеклянный, стекляный, стекляннный"
# ? от нуля до единицы
match=re.findall(r"стеклянн?ый", text)
print(match)
# * любое количество
match=re.findall(r"стеклянн*ый", text)
print(match)
# + от одного повторения, до бесконечности. НЕ ВОЙДЕТ СЛОВО С одной буквой
match=re.findall(r"стеклянн+ый", text)
print(match)