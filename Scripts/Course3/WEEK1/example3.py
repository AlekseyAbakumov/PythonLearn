import re
html="Курс евро на сегодня 68,7514, курс евро на завтра 67,8901"
match=re.search(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
rate=match.group(1)
print(rate)

match=re.search(r'Евро\D+(\d+,\d+)', html)
rete=match is None

y=re.search(r'Евро.*(\d+,\d+)', html, re.IGNORECASE).group(1)
print(y)
y=re.search(r'Евро.*?(\d+,\d+)', html, re.IGNORECASE).group(1)
print(y)
y=re.findall(r'Евро\D+(\d+,\d+)', html, re.IGNORECASE)
print(y)
y=re.findall(r'Евро\D+\d+,\d+', html, re.IGNORECASE)
print(y)