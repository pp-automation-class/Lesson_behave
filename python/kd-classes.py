class BankAccount:
    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'{self.owner_name} deposited ${amount}. New balance: {self.balance}')

    def check_balance(self):
        print(f"{self.owner_name}'s balance: ${self.balance}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds. Please try another amount.')
        else:
            self.balance = self.balance - amount
            print(f'{self.owner_name} withdrawn ${amount}. New balance: {self.balance}')


account1 = BankAccount('John', 300)
account2 = BankAccount('Mary')
account2.check_balance()
account2.deposit(400)
account1.check_balance()
account1.withdraw(150)
account1.withdraw(200)
