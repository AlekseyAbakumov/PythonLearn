# Реализуем паттерн наблюдатель

from abc import ABC, abstractmethod


class NotificationManager:
    """класс, который управляет подпиской на новости"""

    # создаем словарь, с подписчиками
    def __init__(self):
        self.__subscribers = set()

    # метод "Подписаться"
    def subscribe(self, subscriber):
        self.__subscribers.add(subscriber)

    # метод "Отписаться"
    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    # метод "Отправить уведомление подписчикам"
    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)


# создаем Астрактного наблюдателя
class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class MessageNotifier(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} получил сообщение")


class MessagePrinter(AbstractObserver):
    def __init__(self, name):
        self.__name = name

    def update(self, message):
        print(f"{self.__name} получил сообщение: {message}")


notifier = MessageNotifier("Notifier1")
printer1 = MessagePrinter("Printer1")
printer2 = MessagePrinter("Printer2")

manager = NotificationManager()

manager.subscribe(notifier)
manager.subscribe(printer1)
manager.subscribe(printer2)

manager.notify("Привет")
