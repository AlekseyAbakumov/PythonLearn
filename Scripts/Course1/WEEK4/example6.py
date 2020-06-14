# создадим дескриптор, который будет хранить историю в отдельном файле
# Какое значение атрибута было присвоено


class ImportantValue:
    def __init__(self, amount):
        self.amount = amount

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        with open("F:/WORK/log.txt", 'a') as f:
            f.write(str(value) + '\n')

        self.amount = value


class Account:
    amount = ImportantValue(100)


bobs_account = Account()
bobs_account.amount = 200

with open("F:/WORK/log.txt", 'r') as f:
    print(f.read())
