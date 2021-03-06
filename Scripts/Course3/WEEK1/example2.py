import requests
import re

result = requests.get("http://cbr.ru")
html = result.text
print(html)

print("Регулярки")
match = re.search(r'Евро\D+(\d+,\d+)', html)
# Перевод 1:Ищем слово Евро
# 2:\D -Пропускаем все, что не является цифрами
# 3: \D+ Прускаем все, что не является цифрами и это может повториться
#           несколько раз.
# 4: () Круглые скобки обозначают группу. То что находится в группе модуль
#       запоминает и потом это можно достать.
# 5: \d - ищем цифры несколько раз.
# 6: , Ищем запятую.
# 7: \d - вновь ищем цифры.
# За счет того, что мы объединили их в скобки, то здесь все будет возвращено
# в первой группе объекта match
rate = match.group(1)
print(rate)
