# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

  # main-0.py

import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <operation> <amount>")
        print("Operations: deposit, withdraw, balance")
        return

    operation = sys.argv[1].lower()
    try:
        amount = float(sys.argv[2]) if operation in ['deposit', 'withdraw'] else 0.0
    except ValueError:
        print("Please enter a valid numeric amount.")
        return

    account = BankAccount()

    if operation == 'deposit':
        account.deposit(amount)
        print(f"Deposited ${amount:.2f}")
        account.display_balance()
    elif operation == 'withdraw':
        success = account.withdraw(amount)
        if success:
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds. Withdrawal failed.")
        account.display_balance()
    elif operation == 'balance':
        account.display_balance()
    else:
        print("Invalid operation. Use deposit, withdraw, or balance.")

if __name__ == "__main__":
    main()
