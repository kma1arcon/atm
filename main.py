class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            return "Invalid deposit amount"
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return f"New balance: {self.balance}"

    def check_balance(self):
        return f"Current balance: {self.balance}"

new_account = Account("John Doe", 1000)
print(new_account.check_balance())
print(f"Deposit result: {new_account.deposit(500)}")
print(new_account.withdraw(200))
print(new_account.withdraw(1500))
print(f"Deposit result: {new_account.deposit(-500)}")
print(new_account.check_balance())