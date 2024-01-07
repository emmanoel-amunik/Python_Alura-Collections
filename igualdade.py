from operator import attrgetter
from functools import total_ordering


@total_ordering
class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __eq__(self, other):
        if type(other) is not SalaryAccount:
            return False

        return self._code == other.get_code()

    def __lt__(self, other):  # less than
        if self._balance is not other.get_balance:
            return self._balance < other._balance

        return self._code < other.get_code

    def __str__(self):
        return f"<<< Code {self._code} Balance {self._balance}<<<"

    def deposit(self, value):
        self._balance += value

    def get_code(self):
        return self._code

    def get_balance(self):
        return self._balance


account1 = SalaryAccount(37)
print(account1)

account2 = SalaryAccount(37)
print(account2)

print(account1 == account2)    # True
print(account1 in [account2])  # True
print(account2 in [account1])  # True


class MultipleSalaryAccount(SalaryAccount):
    pass


print(isinstance(MultipleSalaryAccount(34), SalaryAccount))  # True


account_of_guilherme = SalaryAccount(1700)
account_of_guilherme.deposit(500)

account_of_daniela = SalaryAccount(3)
account_of_daniela.deposit(1000)

account_of_paulo = SalaryAccount(133)
account_of_paulo.deposit(500)

accounts = [account_of_guilherme, account_of_daniela, account_of_paulo]

for acc in accounts:
    print(acc)

for conta in sorted(accounts, key=attrgetter("_balance", "_code")):
    print(conta)


print(account_of_guilherme < account_of_daniela)  # True

for acc in sorted(accounts):
    print(acc)

for acc in sorted(accounts, reverse=True):
    print(acc)

print("....................")

for acc in sorted(accounts):
    print(acc)

print(account_of_guilherme <= account_of_daniela)
print(account_of_daniela <= account_of_paulo)
print(".....")
print(account_of_guilherme < account_of_guilherme)
print(account_of_guilherme == account_of_guilherme)
print(account_of_guilherme <= account_of_guilherme)
