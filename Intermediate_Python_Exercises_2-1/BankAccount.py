import sys
#Cameron Dennis 

class BankAccount:
    #Class Constructors and iniziliations:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    #Deposit function 
    def deposit(self, amount):
        self.balance += amount

    #Deposit function 
    def withdraw(self, amount):
        self.balance -= amount

    #Deposit function 
    def get_balance(self):
        return f"{self.account_name} has a balance of {self.balance}"

