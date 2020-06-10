# МАГИЧЕСКИЕ МЕТОДЫ


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email_data(self):
        return {
            'name': self.name,
            'email': self.email
        }


jane = User('Jane Doe', 'janedoe@example.com')

print(jane.get_email_data())

print("Без магического метода __str__")
print(jane)


# МАГИЧЕСКИЙ МЕТОД __STR__
# с помощью него можно переопределить, как будет вести себя класс, когда
# обращаемся к его имени
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)


jane = User('Jane Doe', 'janedoe@example.com')

print("С магическим методом __str__")
print(jane)

# методы getattr, getattribute
print("методы getattr, getattribute")


class Researcher:

    # метод определяет что делать, когда обращаемся к несуществующему атрибуту
    def __getattr__(self, item):
        return "Такого атрибута не существует"


x = Researcher()

print(x.attr)


class Researcher2:

    # метод срабатывает каждый раз, когда идет обращение к любому атрибуту
    def __getattribute__(self, item):
        return 'Ха-ха'


x = Researcher2()

print(x.attr)
