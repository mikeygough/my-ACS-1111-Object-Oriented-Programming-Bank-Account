from random import randint

class BankAccount:
    """ BankAccount stores full_name, account_number (randomly generated 8 digit number) and a balance """
    def __init__(self, full_name: str = '', 
                       account_number = randint(10000000, 99999999),
                       balance: float = 0.0,
                       account_type: str = 'checking'):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        
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
            # checking account interest rate
            if self.account_type == 'checking':
                self.balance += round(self.balance * 0.00083, 2)
            # savings account interest rate
            elif self.account_type == 'savings':
                self.balance += round(self.balance * 0.001, 2)
            print(f"Adding Interest")
        else:
            print("Insufficient Funds. Accounts with negative balances cannot accrue interest")
        self.print_balance()
    
    def print_statement(self):
        """ prints the account full_name, account_number and balance. """
        print(self.full_name)
        # blur beginning of account number
        print(f"Account No.: ****{str(self.account_number)[4:]}")
        self.print_balance()
        
    def print_balance(self):
        """ prints the account balance (formatted). """
        print(f"Balance: ${self.balance:.2f}")
    
# TEST 1
odysseus_x = BankAccount(full_name="Odysseus X", balance=100, account_type='savings')
print("Full Name:", odysseus_x.full_name)
print("Account Number:", odysseus_x.account_number)
print("Balance:", odysseus_x.balance)
# DEPOSIT
odysseus_x.deposit(50)
# WITHDRAW
odysseus_x.withdraw(25)
# GET_BALANCE
odysseus_x.get_balance()
# ADD_INTEREST
odysseus_x.add_interest()
# PRINT_STATEMENT
odysseus_x.print_statement()

# TEST 2
bart_s = BankAccount(full_name="Bart Simpson", balance=50)
print("Full Name:", bart_s.full_name)
print("Account Number:", bart_s.account_number)
print("Balance:", bart_s.balance)
# DEPOSIT
bart_s.deposit(5)
# WITHDRAW
bart_s.withdraw(100) # Insufficient Funds. Charging $10 overdraft fee.
# GET_BALANCE
bart_s.get_balance()
# ADD_INTEREST
bart_s.add_interest()
# PRINT_STATEMENT
bart_s.print_statement()

# TEST 3
# Create a new bank account instance: user: "Mitchell", account number: 03141592.
mitchell_h = BankAccount(full_name="Mitchell Hudson", account_number='03141592')
# Deposit $400,000 into "Mitchell's" account.
mitchell_h.deposit(400000)
# Print a statement
mitchell_h.print_statement()
# Add interest to the account
mitchell_h.add_interest()
# Print a statement
mitchell_h.print_statement()
# Make a withdrawl of $150 (Mitchell needs some Yeezy's)
mitchell_h.withdraw(150)
# Print a statement
mitchell_h.print_statement()

bank = [odysseus_x, bart_s, mitchell_h]
for account in bank:
    account.add_interest()