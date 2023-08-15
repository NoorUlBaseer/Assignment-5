"""
Task-1: BankAccount System
1. Create a Python class named BankAccount.
2. Define the following methods within the BankAccount class:
	set_account_details(self, account_number, account_holder_name, initial_balance=0)
	deposit(self, amount)
	withdraw(self, amount)
	display_account_info(self)
3. Create an object of the BankAccount class.
4. Use the set_account_details method to set the account number, account holder's name, and initial balance.
5. Use the deposit and withdraw methods to simulate depositing and withdrawing money from the account.
6. Finally, use the display_account_info method to print the account details.
"""

class BankAccount:
    def set_account_details(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def display_account_info(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Balance:", self.balance)

account = BankAccount()
acc_number = input("Enter Account Number: ")
acc_holder_name = input("Enter Account Holder Name: ")
account.set_account_details(acc_number, acc_holder_name)

deposit_amount = int(input("Enter Deposit Amount: "))
account.deposit(deposit_amount)

withdraw_amount = int(input("Enter Withdraw Amount: "))
account.withdraw(withdraw_amount)

print()
account.display_account_info()