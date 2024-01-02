class CurrentAccount:
    def __init__(self, code):
        self.code = code
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def __str__(self):
        return f"[>>Code {self.code} Balance {self.balance}<<<]"


account_of_gui = CurrentAccount(15)
print(account_of_gui)
account_of_gui.deposit(500)
print(account_of_gui)

account_of_dani = CurrentAccount(47685)
account_of_dani.deposit(1000)
print(account_of_dani)

accounts = [account_of_gui, account_of_dani]
for account in accounts:
    print(account)


def deposit_to_all(all_accounts):
    for the_account in all_accounts:
        the_account.deposit(100)


accounts = [account_of_gui, account_of_dani]
print(accounts[0], accounts[1])
deposit_to_all(accounts)
print(accounts[0], accounts[1])


guilherme = ("Guilherme", 37, 1981)  # Tuple
daniela = ("Daniela", 31, 1987)
# paulo = (35, "Paulo", 1979)  # wrong


conta_do_gui = (15, 1000)


def deposit(in_account):
    new_balance = in_account[1] + 100
    code = in_account[0]
    return code, new_balance


deposit(conta_do_gui)  # Não funciona
conta_do_gui = deposit(conta_do_gui)  # Precisa ser re-atribuído
