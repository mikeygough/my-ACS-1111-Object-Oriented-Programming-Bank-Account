from random import randint

class BankAccount:
    def __init__(self, full_name: str = '', 
                       account_number = randint(10000000, 99999999),
                       balance: float = 0.0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount: float):
        self.balance += amount
        print(f"Amount deposited: ${amount}")
        print(f"New balance: ${self.balance}")
        
    def withdraw(self, amount: float):
        if amount > self.balance:
            self.balance -= 10
            print("Insufficient Funds. Charging $10 overdraft fee.")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount}")
            print(f"New balance: ${self.balance}")
    
    def get_balance(self):
        print(f"Current balance: ${self.balance}")
        return self.balance
    
    def add_interest(self):
        self.balance += self.balance * 0.00083
        print(f"Adding Interest")
        print(f"Current balance: ${self.balance}")
    
    def print_statement(self):
        pass
    
# TESTING

# INIT
account = BankAccount(full_name="Odysseus X", balance=100)
print("Full Name:", account.full_name)
print("Account Number:", account.account_number)
print("Balance:", account.balance)

# DEPOSIT
account.deposit(50) # -> balance = 150

# WITHDRAW
account.withdraw(25) # -> balance = 125
# account.withdraw(126) # -> "Insufficient Funds. Charging $10 overdraft fee."

# GET_BALANCE
account.get_balance() # -> "Current balance: $125". Returns self.balance

# ADD_INTEREST
account.add_interest() # -> "Adding Interest\n Current balance: $125.10375". balance = 125.10375