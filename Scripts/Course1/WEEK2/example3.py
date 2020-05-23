# СЛОВАРИ
# Позволяют хранить данные в формате Ключ-значение
empty_dict = {}
empty_dict = dict()

collections_map = {
    'multable': ['list', 'set', 'dict'],
    'imultable': ['tuple', 'frozenset']
}
print(collections_map)
print(
    "Ключи словаря, благодаря хэшированию, позволяют получить значение по "
    "ключу за константное время")
print(collections_map['imultable'])

print(collections_map.get('несуществующий ключ', 'Дефолтное значение'))

x = 'multable' in collections_map  # Проверяем, есть ли ключ в словаре
y = 'несуществующий ключ' in collections_map
print(x, y)

# Добавление элементов в словарь
print("Добавление элементов в словарь")
Beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar'
}
print(Beatles_map)
Beatles_map['Ringo'] = 'Drums'  # Добавить значение в словарь
print(Beatles_map)
del Beatles_map['John']  # Удалить значение из словаря
print(Beatles_map)
Beatles_map.update({  # Обновление словаря
    'Paul': 'Super Bass',  # Если ключ есть, то значение обновится
    'Joht': 'Guitar'  # Если ключа нет, то значение добавится
})
print(Beatles_map)

print("Если ключа нет, то еще можно добавить в качестве значение Дефолт")
Beatles_map.setdefault('Paul', 'default')  # Этот ключ в словаре есть. С ним
# не делают
Beatles_map.setdefault('key', 'default')  # Этого ключа нет. Он добавляется
# и значение ставится дефолтное
print(Beatles_map)

# Итерация по словарю, с выводом ключей
print("Итерация по ключам словаря")
for i in Beatles_map:
    print(i)

# Итерация по словарю, с выводом значение
for i in Beatles_map.values():
    print(i)

# Итерация по словарю, с выводом Ключ - значение
for a, b in Beatles_map.items():
    print('{} --- {}'.format(a, b))

# По дефолту, данные в словаре могут хранится в неупорядоченном виде. Это
# норма. Если нужно обязательно хранить в нужном порядке, тогда словарь нужно
# создаватьс помощью отдельного модуля
from collections import OrderedDict

mySlovar = OrderedDict()  # создается словарь, в котором значения будут
# храниться в том порядке, в каком они были добавлены
mySlovar['myKey'] = 'myValue'
mySlovar['myKey2'] = 'myValue2'
print(mySlovar)
