# Bank Account (OOP with deposit & withdraw)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")
        else:
            print("Insufficient funds!")

# Example usage
acc = BankAccount("Ayush", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.withdraw(2000)
