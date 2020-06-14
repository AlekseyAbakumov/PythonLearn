# контекстные менеджеры
# С подобным уже работали.
# Данный менеджер следит, чтобы в конце файл был закрыт

with open('filename', 'r') as f:
    f.read('filename')


# Можно создать свой контекстный менеджер
class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    # мы обратились через функцию, создали объект класса. Затем мы возвращаем
    # конструкцию "as f" через магический метод ENTER
    def __enter__(self):
        return self.f

    # магический метод EXIT отвечает за то, что делать при выходе из блока
    # контекстного менеджера
    def __exit__(self, *args):
        self.f.close()


with open_file('filename', 'r') as f:
    x = f.read()
