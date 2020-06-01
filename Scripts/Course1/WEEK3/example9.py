# МЕТОДЫ КЛАССА


class Event:
    # Описание события и даты, когда оно происходит
    def __init__(self, description, event_date):
        self.desctiption = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.desctiption}\" at {self.date}"


from datetime import date

event_description = "Рассказать, что такое метод класса"
event_date = date.today()

event = Event(event_description, event_date)
print(event)


# Данная программа ответчает, чтобы заносить в календарь данные от пользователя

# Данные, которые якобы ввел пользователь
def extract_description(user_input):
    return "отмена Скрама"


def extract_date(user_input):
    return date(2020, 7, 5)


class EventUser:

    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"EventUser \"{self.description}\" at {self.date}"

    # Декоратор @classmethod - это встроенный объект. Его не нужно ни откуда
    # грузить. Этот декоратор делает МЕТОД, МЕТОДОМ класса
    @classmethod
    def from_string(cls, user_input):
        # Это будто мы с помощью хитрых функций вырезали из текста нужный нам
        # кусок с событием и датой. На самом деле, они определены выше
        description = extract_description(user_input)
        date = extract_date(user_input)
        # возвращаем элемент класса
        return cls(description, date)


event = EventUser.from_string("добавь в календарь отмена Скрама, 5 июля 2020")
print(event)
