# для отработки
class FileReader:
    """Класс для чтения данных из документа"""

    def __init__(self, fullname):
        self.fullname = fullname

    def read(self):
        """Метод чтения данных из файла"""
        try:
            with open(self.fullname, 'r', encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            return ""


x = FileReader("F:/WORK/test.txt")  # Существует
y = x.read()
print(y)

x = FileReader("F:/WORK/test2.txt")  # Не существует
y = x.read()
print(y)
