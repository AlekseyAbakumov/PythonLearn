# Задача на словари. Нужно найти тре самых встречающихся слова в текст.перемен
zen = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# Ключ - это слово. Значение - количество, сколько раз оно встречается
# Если ключа нет, то его нужно добавить. Если он есть, то значение + 1
zen_map = {}
for word in zen.split():  # Сплит разобьет фразу по пробелам
    cleaned_word = word.strip('.,!-*').lower()  # Очистим переменную от
    # ненужных символов + приведем к нижнему регистру
    if cleaned_word in zen_map:  # Ключ есть в словаре
        zen_map[cleaned_word] += 1  # Изменить значение ключа
    else:  # Ключа нету
        zen_map[cleaned_word] = 1

import operator

zen_items = zen_map.items()  # Из словаря получаем список кортежей Tuple
# Отсортировать в обратном порядке
word_count_items = sorted(zen_items, key=operator.itemgetter(1), reverse=True)
print(word_count_items[:3])  # Показать первые три значения

# ВТОРОЙ СПОСОБ РЕШЕНИЯ
from collections import Counter

cleaned_list = []
for word in zen.split():  # Идем циклом по dict, в качетве разделиля - Space
    # Добавить в список очищенное слово, в нижнем регистре
    cleaned_list.append(word.strip(('.,-!*')).lower())
# Вытащим первые три значение оператором Counter
print(Counter(cleaned_list).most_common(3))
