# Строковые и байтовые строки
print("Строки")
example_string = "Курс про Python на Coursera"
print(example_string)
print(type(example_string))

# Если нужны кавычки, то используем экранирование
example_string = "Курс про \"Python\" на \"Coursera\""
print(example_string)

# "Сырые строки позволяют не использовать экранирование самих слешей"
example_string = "C:\\\\"  # Используя экранирование
print(example_string)
example_string = r"C:\\"  # Используя сырые строки
print(example_string)

# Разбить длинный текст на строки
example_string = "Perl - это тот язык, который одинаково " \
                 "выглядит как до, так и после RSA шифрования " \
                 "(Keith Bostic)"
print(example_string)

# Можно подавать полное форматирование через тройные кавычки
example_string = """
Есть всего два типа языков программирования: те, на которые
люди все время ругаются, и те, которые никто не использует.

Bjarne Stroustrup
"""
print(example_string)
# Объединить две строки в одну
print("Объединить две строки в одну")
x = "Можно просто " + "складывать строки"
print(x)
print("Умножать строки")
x = ("Hello" * 3)
print(x)

# адрес объекта в памяти
print(id(example_string))
# Строка неизменяемая, если мы меняем переменную, то меняется и адрес

# Срезы строк
example_string = "Курс про Python на Coursera"
print(example_string[:4])  # Stop
print(example_string[9:])  # Start
print(example_string[5:8])  # Between
print(example_string[0:28:2])  # Start, Stop, Step. Каждую вторую букву
print(example_string[::2])  # Аналогично. Каждую вторую букву
print(example_string[-8:])  # Символов от конца строки
# Развернуть текст
example_string = "Москва"
print(example_string[::-1])
# Можно узнать количество вхождение символов
print("Можно узнать количество вхождение символов")
example_string = "Райффайзенбанк"
print(example_string.count("ф"))  # Сколько раз встречается буква "ф"
# Работа с текстом
print("Преобразования текста")
x = "райффайзенбанк"
print(x.capitalize())  # Сделать первую букву заглавной

# Наличие строки в строке
x = "Хорошо в деревне летом"
y = "деревне"
z = y in x
print(z)

# Можно итерироваться по строке
example_string = "Hello"
for i in example_string:
    print(i)

# Форматирование строк
print("Форматирование строк")
# Подставит значения с помощью placeholder
# Первый вариант
template = "%s - главное достоинство программиста. (%s)"
print(template)
print(template % ("Лень", "Larry Wall"))
# Второй вариант подстановки с placeholder
template = "{} не лгут, но {} пользуются формулами. ({})"
print(template)
print(template.format("Цифры", "лжецы", "Robert A. Heinlein"))
# Третий способ. с помощью "именнованных" placeholder
template = "{num} КБ должно хватить для любых задач. ({author})"
print(template)
print(template.format(num=640, author="Bill Gates"))
# Четвертый, самый удобный. Это f-строки
subject = "оптимизация"
author = "Donald Knuth"
template = f"Преждевременная {subject} - корень всех зол. ({author})"
print(template)

# Ввод данных от пользователя
name = input("Введите имя: ")
myName = f"Привет, {name} !"
print(myName)
