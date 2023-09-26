"""Problem 3: Bank Account Management Using Class and Objects 
Create a Python class called BankAccount with attributes account_number, account_holder, and balance. Implement methods deposit and withdraw to add and subtract funds from the account's balance, respectively. Additionally, create a method display_balance to display the current balance of the account. Create an object of the BankAccount class, perform multiple deposits and withdrawals, and display the final balance."""


class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self):
        add_balance = float(input("Enter the amount to deposit: "))
        if add_balance > 0:
            self.balance += add_balance
            print(
                f"Your deposited {add_balance} tk has been successfully added to your Acc balance.")
            print("------------------------------")
            total_balance = initial_balance + add_balance
            print("Total Balance:", total_balance)
            print("==============================")

    def withdraw(self):
        withdraw_balance = float(input("Enter the amount to withdraw: "))
        if withdraw_balance > 0 and withdraw_balance <= self.balance:
            self.balance -= withdraw_balance
            print(
                f"Your withdrew {withdraw_balance} tk has been successfully completed.")
            print("==============================")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def view(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance} tk")
        print("Thank you for Banking with us:)")


try:
    account_number = int(input("Enter your account number: "))
except ValueError:
    print("Value Errors")
# account_holder = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
# ====================objects============
acc1 = BankAccount(account_number, "Jaman", initial_balance)

acc1.deposit()
acc1.withdraw()
acc1.view()
