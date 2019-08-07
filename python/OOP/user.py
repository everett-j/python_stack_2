class User:
    def __init__(self, username, email_address, account):
        self.name = username
        self.email = email_address
        self.account = BankAccount(interest_rate=0.02, balance=0)
    
    def make_deposit (self, amount):
        self.account.balance()
        print(self.account.balance)

    def make_withdrawl (self, amount):
        self.account.balance()
        print(self.account.balance)

    def display_user_balance (self):
        self.account_balance
        print(self.account.balance)

    def transfer_money (self, other_user, amount):
        self.account_balance += amount
        other_user.account_balance -= amount
        self.account_balance
        other_user.account_balance
        print(self.account.balance)

josh = User("Josh Everett", "jseverett16@gmail.com")
britt = User("Brittany Everett", "brittanyja2016@gmail.com")
addison = User("Addison Everett", "munchkineverett@gmail.com")

class BankAccount:
    def __init__(self, interest=0.02, balance=0):
        print(self.interest = interest_rate)
        print(self.balance = account_balance)
    
    def deposit (self, amount):
        print(self.account_balance += amount)

    def withdrawl (self, amount):
        if self.account_balance < 0:
            self.account balance -= 5
        print(self.account_balance -= amount)

    def display_account_info (self):
        print ("Balance: $" self.account_balance)  

    def yield_interest (self):
        if account_balance > 0
            print(self.account_balance * interest_rate)  

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance=0):
    	super().__init__(int_rate, balance)	
        self.is_roth = is_roth	

    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
            super().withdraw(amount)
            return self

account1 = BankAccount()
account2 = BankAccount()
account3 = BankAccount()