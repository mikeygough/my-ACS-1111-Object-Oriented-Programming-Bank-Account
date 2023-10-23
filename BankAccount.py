from random import randint

class BankAccount:
    """ BankAccount stores full_name, account_number (randomly generated 8 digit number) and a balance """
    def __init__(self, full_name: str = '', 
                       account_number = randint(10000000, 99999999),
                       balance: float = 0.0):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, amount: float):
        """ increase balance by the amount. """
        self.balance += amount
        print(f"Amount deposited: ${amount}")
        self.print_balance()
        
    def withdraw(self, amount: float):
        """ reduce balance by the amount. error if amount > balance. """
        if amount > self.balance:
            self.balance -= 10
            print("Insufficient Funds. Charging $10 overdraft fee.")
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount}")
            self.print_balance()
    
    def get_balance(self):
        """ prints and returns the account balance. """
        self.print_balance()
        return self.balance
    
    def add_interest(self):
        """ if account balance > 0 then add 0.083% interest to the account balance. """
        if self.balance >= 0:
            self.balance += round(self.balance * 0.00083, 2)
            print(f"Adding Interest")
        else:
            print("Insufficient Funds. Accounts with negative balances cannot accrue interest")
            self.print_balance()
    
    def print_statement(self):
        """ prints the account full_name, account_number and balance. """
        print(self.full_name)
        print(f"Account No.: ****{str(self.account_number)[4:]}")
        self.print_balance()
        
    def print_balance(self):
        """ prints the account balance (formatted). """
        print(f"Balance: ${self.balance:.2f}")
    
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

# PRINT_STATEMENT
account.print_statement() # -> "Odysseus X" "Account No.: ****3285" "Balance: $125.10375"