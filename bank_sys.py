class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")
    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")

if __name__ == "__main__":
    # instance
    account1 = BankAccount("123456", "Alice", 500)

    # Display 
    account1.display_account_info()

    # Deposit
    account1.deposit(200)

    # Withdraw money
    account1.withdraw(150)

    # Attempt to withdraw more than the balance
    account1.withdraw(600)

    # Final account stats
    account1.display_account_info()
