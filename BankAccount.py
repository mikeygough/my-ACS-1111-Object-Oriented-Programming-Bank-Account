from random import randint

class BankAccount:
    def __init__(self, full_name: str = '', 
                       account_number = randint(10000000, 99999999),
                       balance: float = 0.0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        
account = BankAccount()
print(account.account_number)