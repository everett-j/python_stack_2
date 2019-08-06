class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit (self, amount)
        self.account_balance += amount

    def make_withdrawl (self, amount)
        self.account_balance -= amount

    def display_user_balance (self)
        self.account_balance

    def transfer_money (self, other_user, amount)
        self.account_balance += amount
        other_user.account_balance -= amount
        self.account_balance
        other_user.account_balance

josh = User("Josh Everett", "jseverett16@gmail.com")
britt = User("Brittany Everett", "brittanyja2016@gmail.com")
addison = User("Addison Everett", "munchkineverett@gmail.com")

class BankAccount:
    def __init__(self)
    self.interest = interest_rate
    self.interest_rate = 0.01
    self.account_balance = 0
    
    def deposit (self, amount)
        self.account_balance += amount

    def withdrawl (self, amount)
        self.account_balance -= amount

    def display_account_info (self)
        print ("Balance: $" self.account_balance)  

    def yield_interest (self)
       if account_balance > 0:
            print(self.account_balance * interest_rate)  