# Синхронизация, блокировки потоков

import threading

# создаем два объекта класса БЛОКИРОВКА
a = threading.RLock()
b = threading.RLock()


def foo():
    try:
        # Метод acquire - получить/захватить блокировку
        a.acquire()
        b.acquire()
    finally:
        # метод release - высвободить блокировку
        a.release()
        b.release()
