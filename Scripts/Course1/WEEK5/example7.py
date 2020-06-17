# Синхронизация потоков, условные переменные

import threading


class Queue(object):
    # Создаем очередь. Равную 5
    def __init__(self, size=5):
        self._size = size
        self._queue = []
        self._mutex = threading.RLock()
        # создаем две условные переменные, которые получают объект блокировки
        self._emgty = threading.Condition(self._mutex)
        self._full = threading.Condition(self._mutex)

    def put(self, val):
        with self._full:
            # Если пытаемся выполнять операцию, а очередь переполнена
            while len(self._queue) >= self._size:
                # то ставить на ожидание
                self._full.wait()

            self._queue.append(val)
            # оповещаем все потоки, которые ждут освобождения очереди
            self._emgty.notify()

    def get(self):
        with self._emgty:
            while len(self._queue) == 0:
                self._emgty.wait()

            ret = self._queue.pop(0)
            self._full.notify()
            return ret
