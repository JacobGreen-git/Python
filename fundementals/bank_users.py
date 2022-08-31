class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = (self.balance + amount)
        # print(f"Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        self.balance = (self.balance - amount)
        # print(f"Balance: {self.balance}")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        # print(f"Balance: {self.balance}")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = .02, balance = 0)

    def display_info(self):
        print(self.name)
        print(self.email)
        print(self.account.balance)

    def make_deposit (self, amount):
        self.account.deposit(amount)
        print(self.account.balance)


Joe = User('Joe Shmo', 'jdsibfvi@gmail.com')


Joe.make_deposit(300)
Joe.display_info()