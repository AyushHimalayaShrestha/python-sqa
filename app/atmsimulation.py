# Atm Simulation
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")

atm = ATM(1000)
atm.check_balance()
atm.deposit(500)
atm.withdraw(200)
atm.withdraw(2000)
