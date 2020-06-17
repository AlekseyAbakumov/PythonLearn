import time
from threading import Thread

# операция, с нагрузкой на ЦП
print("Операция с нагрузкой на ЦП")
print("")
print("В одном потоке")


# В одном потоке
def myCount(sum_count):
    for i in range(sum_count):
        a = 1
        a += 1
        if a != 1:
            a -= 1


t0 = time.time()

myCount(100_000_000)
myCount(100_000_000)

print(time.time() - t0)

print("")
print("В двух потоках")

# В двух потоках
t1 = time.time()

th1 = Thread(target=myCount, args=(100_000_000,))
th2 = Thread(target=myCount, args=(100_000_000,))

th1.start()
th2.start()

th1.join()
th2.join()

print(time.time() - t1)

# операция, с нагрузкой на память
print("Операция с нагрузкой на память")
print("")
print("В одном потоке")


# В одном потоке
def myText(sum_count):
    for i in range(sum_count):
        print("aaa")


t0 = time.time()

myText(10_000_000)
myText(10_000_000)

# Время в одном потоке
t1 = time.time() - t0

# В двух потоках
t2 = time.time()

th1 = Thread(target=myText, args=(10_000_000,))
th2 = Thread(target=myText, args=(10_000_000,))

th1.start()
th2.start()

th1.join()
th2.join()

t3 = time.time()-t2

print("Время в одном потоке")
print(t1)
print("Время в двух потоках")
print(t3)
