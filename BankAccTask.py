class Bank_Account:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of Rupees {amount}  is successful. New balance: {self.balance}/-")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal of Rupees {amount}  is successful. New balance: {self.balance}/-")
            else:
                print("Insufficient funds. Withdrawal unsuccessful.")
        else:
            print("Invalid withdrawal amount. Please withdraw a positive amount.")

    def display_balance(self):
        print(f"Current balance for account {self.account_number}: {self.balance}/-")

#create a bank account
account1 =Bank_Account("Deepu",6304785433,10000)

#display intial balance
account1.display_balance()

#deposit money
account1.deposit(5000)

#withdraw money
account1.withdraw(3000)

#withdraw more than balance
account1.withdraw(20000)

#displaying final balance
account1.display_balance()

print("\n Another Account holder\n")
account2 =Bank_Account("Jhonny",123456789,50000)
account2.deposit(25000)
account2.withdraw(13000)
account2.withdraw(33000)
account2.display_balance()