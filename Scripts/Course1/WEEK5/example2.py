# Создание потока

# Первый вариант, прямой
# Потоки выполняются в рамках одного процесса
# У каждого есть свой стек.
# Управление и выполнение потоков занимается ОС

from threading import Thread

# Функция, которую хотим выполнять в отдельном потоке
def f(name):
    print("hello", name)

# создаем новый поток
th = Thread(target=f, args=("Bob",))
# запускаем поток
th.start()
# дожидаемся окончания всех потоков в процессе
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
