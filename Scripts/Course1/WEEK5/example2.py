# Создание потока

# Первый вариант, прямой

from threading import Thread


def f(name):
    print("hello", name)


th = Thread(target=f, args=("Bob",))
th.start()
th.join()


# Второй вариант, через классы
class PrintThread(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello", self.name)


th = PrintThread("Mike")
th.start()
th.join()
