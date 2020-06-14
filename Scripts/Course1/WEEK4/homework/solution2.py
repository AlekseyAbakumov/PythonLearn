# написать дескриптор, который будет вычитать коммисию


class Value:
    def __init__(self):
        self.amount = 0

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        self.amount = value - value * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


# x = Account(0.1)
# x.amount = 100
#
# print(x.amount)
