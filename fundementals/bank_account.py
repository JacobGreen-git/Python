
class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        # print(f"Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        self.balance -= amount
        # print(f"Balance: {self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        # print(f"Balance: {self.balance}")
        return self

acct1 = BankAccount(.01, 500)
acct2 = BankAccount(.01, 1500)


acct1.deposit(200).deposit(25).deposit(400).withdraw(300).yield_interest().display_account_info()
acct2.deposit(10000).deposit(25000).withdraw(200).withdraw(340).withdraw(25).withdraw(2500).yield_interest().display_account_info()

