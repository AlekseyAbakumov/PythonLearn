# создание пула потоков

from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


# .shutdown() in exit

with ThreadPoolExecutor(max_workers=3) as pool:  # Максимальное количество
    # потоков

    # метод submit создает объект типа concurrent.futures.Future
    # Это такой объект, который еще не завершился, но выполняется и будет
    # завершен в будущем
    results = [pool.submit(f, i) for i in range(10)]

    for future in as_completed(results):
        print(future.result())
