# СОКЕТЫ

# Сервер

import socket

# https://docs.python.org/3/library/socket.html
# создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# используем метод bind. Ему нужен хост и порт
# Порты лучше использовать более 2000, т.к. они чаще всего зарезервированы
# системой
sock.bind(("127.0.0.1", 10001))  # max port 65535
# сокет начинает принимать соединения
sock.listen(socket.SOMAXCONN)

# Это само создание канала соединения.
conn, addr = sock.accept()
while True:
    # если соединение закрылось, то нужно прекратить программу
    data = conn.recv(1024)
    if not data:
        break
    # process data
    print(data.decode("utf8"))

conn.close()
sock.close()
