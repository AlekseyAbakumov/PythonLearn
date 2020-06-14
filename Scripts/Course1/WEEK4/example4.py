# пишем контекстный менедежер, задачей которого будет считать время,
# проведенное внутри него
import time


class timer:

    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        pass

    def __exit__(self, *args):
        self.end = time.time()
        print('Программа работала {} секунд'.format(self.end - self.start))


with timer():
    time.sleep(1)
