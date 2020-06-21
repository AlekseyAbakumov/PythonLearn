# СОКЕТЫ

# Клиент

import socket

# создать потоковый сокет
# sock = socket.socket()
# использовать метод connetc. Он блокируется, пока сервер со своей стороны
# не вызовет метод accept
# sock.connect(("127.0.0.1", 10001))
# используем метод sendall, чтобы начать получить данные с сервера
# sock.sendall("ping".encode("utf8"))
# sock.close()

# более короткая запись
sock = socket.create_connection(("127.0.0.1", 10001))
sock.sendall("ping".encode("utf8"))
sock.close()
