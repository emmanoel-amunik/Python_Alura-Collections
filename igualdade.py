from operator import attrgetter


class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __eq__(self, other):
        if type(other) is not SalaryAccount:
            return False

        return self._code == other.get_code()
        # and self._balance == other._balance

    def __lt__(self, other):
        return not self._balance > other._balance

    def __str__(self):
        return f"<<< Code {self._code} Balance {self._balance}<<<"

    def deposit(self, value):
        self._balance += value

    def get_code(self):
        return self._code


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


account_of_guilherme = SalaryAccount(17)
account_of_guilherme.deposit(500)

account_of_daniela = SalaryAccount(3)
account_of_daniela.deposit(1000)

account_of_paulo = SalaryAccount(33)
account_of_paulo.deposit(510)

accounts = [account_of_guilherme, account_of_daniela, account_of_paulo]

for acc in accounts:
    print(acc)

for conta in sorted(accounts, key=attrgetter("_balance")):
    print(conta)


print(account_of_guilherme < account_of_daniela)  # True

for acc in sorted(accounts):
    print(acc)

for acc in sorted(accounts, reverse=True):
    print(acc)
