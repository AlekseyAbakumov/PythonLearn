# Интерфейс по работе с файлами
import os
import tempfile

# готовим тренировчный файл
path_to_file = "F:/WORK/test.txt"
path_to_file2 = "F:/WORK/test2.txt"
path_to_file3 = "F:/WORK/test3.txt"
with open(path_to_file, 'w', encoding="utf-8") as f:
    f.write("Пусть сдохнет Скрам")
with open(path_to_file2, 'w', encoding="utf-8") as f:
    f.write("Пусть сдохнут два пидора, что придумали Скрам")


class File:
    """Класс, отвечающий за работу с файлами"""

    def __init__(self, path):
        self.path = path
        self.position = 0
        if not os.path.exists(self.path):
            f = open(self.path, 'w')
            f.close
        self.temp_path = tempfile.gettempdir()

    # метод, отвечающий за чтение
    def read(self):
        with open(self.path, 'r', encoding="utf-8") as f:
            return f.read()

    # метод отвечающий за запись
    def write(self, tell_text):
        with open(self.path, 'w', encoding="utf-8") as f:
            f.write(tell_text)

    # переопределяем сложение двух объектов
    def __add__(self, obj):
        # new_path = str(os.path.dirname(self.path)) + str(
        #     os.path.basename(self.path)) + "_1"
        new_path = os.path.join(self.temp_path, "_temp.txt")
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())
        return new_file

    # по заданию print должен возвращать полный путь до файла
    def __str__(self):
        return self.path

    # создаем свой итератор
    def __iter__(self):
        return self

    # определяю, что будет происходить при итерации
    def __next__(self):
        with open(self.path, 'r', encoding="utf-8") as f:
            f.seek(self.position)

            myLine = f.readline()
            if not myLine:
                raise StopIteration

            self.position = f.tell()
            return myLine


x = File(path_to_file)
print(x.path)
print(x.temp_path)
x2 = File(path_to_file2)
print(x.path)

y = x.read()
print(y)
y2 = x2.read()
print(y2)

x.write("И сдохнет много раз")
y = x.read()
print(y)

x3 = x + x2
print(x3)

print(x3.read())

x = File(path_to_file3)

for line in x:
    print(ascii(line))
'line1\n'

# ЭТА ЧАСТЬ ЧИСТИТ ВНОВЬ СОЗДАННЫЙ ВРЕМЕННЫ МУСОР
os.remove("C:/Users/User/AppData/Local/Temp/_temp.txt")
