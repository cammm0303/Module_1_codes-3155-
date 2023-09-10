import sys
#Cameron Dennis 

#import the BankAccount Class
from BankAccount import BankAccount

#Make a new instance of BankAccount:
account = BankAccount('John', 5000)

#Deposit and withdraw 
account.deposit(1000)
account.withdraw(500)

print(account.get_balance())