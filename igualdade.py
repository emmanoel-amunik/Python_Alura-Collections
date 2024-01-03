class SalaryAccount:
    def __init__(self, code):
        self._code = code
        self._balance = 0

    def __eq__(self, other):
        if type(other) is not SalaryAccount:
            return False

        return self._code == other.get_code()
        # and self._balance == other._balance

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
