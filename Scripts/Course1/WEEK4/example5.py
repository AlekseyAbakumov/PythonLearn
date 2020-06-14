# ДЕСКРИПТОРЫ
# С помощью дескрипторов мы можем переопределить, что будет происходить с
# атрибутами класса

class Descriptor:
    # Что делать при обращении к атрибуту
    def __get__(self, obj, obj_type):
        print('get')

    # Что делать при внесении изменении в атрибут
    def __set__(self, obj, obj_type):
        print('set')

    # Что делать при удалении атрибута
    def __delete__(self, obj):
        print('delete')


class Class:
    # Создаем классу атрибут, при этом указываем, чтобы она ссылался
    # на дескрипторы
    attr = Descriptor()


instance = Class()
instance.attr
instance.attr=10
del instance.attr
