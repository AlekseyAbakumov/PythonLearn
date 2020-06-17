# СИНХРОНИЗАЦИЯ ПОТОКОВ

# Очереди, модуль queue
from queue import Queue
from threading import Thread


def worker(q, n):
    while True:
        # получить сообщение из очереди
        item = q.get()
        if item is None:
            break
        print("process data:", n, item)


# Создаем объект, типа ОЧЕРЕДЬ, с макс=5
q = Queue(5)
# В случае, если мы попытаемся поместить в очередь больше, чем размер, то
# это заблокирует поток и будет ждать, пока в потоке не появится свободное
# место

# создаем два потока. q - это очередь
th1 = Thread(target=worker, args=(q, 1))
th2 = Thread(target=worker, args=(q, 2))
th1.start()
th2.start()

for i in range(50):
    # помещаем в очередь
    q.put(i)

# В Python нет аварийного завершения потока. Поэтому тут мы помещаем в очередь
# None, а функция выше, при его проверке, делаем break

q.put(None)
q.put(None)
th1.join()
th2.join()

# Вышеописанные действия выполнялись в два потока параллельно
