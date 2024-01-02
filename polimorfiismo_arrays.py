import numpy as np
from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def deposit(self, value):
        self._balance += value

    def __str__(self):
        return f"[>>> Code {self._code} Balance {self._balance}<<<]"

    @abstractmethod
    def pass_the_month(self):
        pass

# print(Account(88))


class CurrentAccount(Account):
    def pass_the_month(self):
        self._balance -= 2


class SavingAccount(Account):
    def pass_the_month(self):
        self._balance *= 1.01
        self._balance -= 3


class InvestmentAccount(Account):
    pass


"""
account16 = CurrentAccount(16)
account16.deposit(1000)
account16.pass_the_month()
print(account16)

account17 = SavingAccount(17)
account17.deposit(1000)
account17.pass_the_month()
print(account17)
"""

account16 = CurrentAccount(16)
account16.deposit(1000)
account17 = SavingAccount(17)
account17.deposit(1000)
accounts = [account16, account17]

for acc in accounts:
    acc.pass_the_month()
    print(acc)


numbers = np.array([1, 3.5])
print(numbers)
numbers + 3  # n funciona
print(numbers)


account18 = InvestmentAccount(18)
