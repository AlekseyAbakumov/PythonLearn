import requests

# Простой запрос
print("Простой запрос")
r = requests.get('http://httpbin.org/get')
print(r.text)

# Простой подзапрос
print("Простой подзапрос")
r = requests.get('http://httpbin.org/post')
print(r.text)

# Запрос с передачей параметров
print("Запрос с передачей параметров")
payload = {'key1': 'value1',
           'key2': 'value2'
           }
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)

# Передача данных в post put patch запросах
print("Передача данных в post put patch запросах")
r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r.text)

# Передача в запрос json. Первый способ, "ручной" встроенный метод в requests
print(
    'Передача в запрос json. Первый способ, "ручной" встроенный метод в '
    'requests')
import json

url = 'http://httpbin.org/post'
r = requests.post(url, json.dumps({'key': 'value'}))
# либо так
r = requests.post(url, json={'key': 'value'})
print(r.text)

# Передача файла на сервер
print("Передача файла на сервер")
url = 'http://httpbin.org/post'
files = {'file':
             ('test.txt',
              open('F:/WORK/test.txt',
                   'rb'))}
r = requests.post(url, files=files)
print(r.text)

# Передача заголовков
print("Передача заголовков")
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.text)

# Получение ответов от сервера text, content, json
print("Получение ответов от сервера text, content, json")
r = requests.get('http://httpbin.org/get')
print("text")
print(type(r.text), r.text)
print("content")
print(type(r.content), r.content)
print("json")
print(type(r.json()), r.json())
print("Статус ответа")
print(r.status_code)
print("Сравнение статуса с константами из библиотеки request")
print(r.status_code == requests.codes.ok)

# Посмотреть заголовки http ответа
print("Посмотреть заголовки http ответа")
print(r.headers)

# Ответ сервера 301 говорит о том, что запрос был перенаправлен
# В нашем случае обращались к http, а перебросило на https
print("Нас перенаправили")
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

# Запрет на перенаправление
print("Запрет на перенаправление")
r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)

# Куки
print("Куки")
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# Сессии. В рамках одной сессии будут использоваться постоянные куки
print("Сессии")
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)

# Выбрасываение исключение по коду
print("Выбрасывание исключений по коду")
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()
