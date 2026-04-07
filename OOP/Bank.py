class BankAccount:
    def __init__(self):
        # Step 1: Initialize balance to 0
        self.balance = 0

    def deposit(self, amount):
        # Step 4a & 4b: Check that amount is an integer and positive
        if not isinstance(amount, int):
            raise ValueError("Deposit amount must be an integer.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        # Add to balance and print
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        # Step 4a & 4b: Check that amount is an integer and positive
        if not isinstance(amount, int):
            raise ValueError("Withdraw amount must be an integer.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        # Subtract from balance and print
        self.balance -= amount
        print(f"Balance after withdrawal: {self.balance}")


# Step 2: Create instances and check
account1 = BankAccount()
account2 = BankAccount()

print(isinstance(account1, BankAccount))  # True
print(isinstance(account2, BankAccount))  # True

# Step 3 & 4: Testing deposit and withdraw
account1.deposit(100)     # Balance after deposit: 100
account1.withdraw(50)     # Balance after withdrawal: 50

# Uncomment these to see ValueError in action
# account1.deposit(-200)       # ValueError: Deposit amount must be positive.
# account1.deposit("Hello")    # ValueError: Deposit amount must be an integer.
# account1.withdraw(-10)       # ValueError: Withdraw amount must be positive.
# account1.withdraw("Bye")     # ValueError: Withdraw amount must be an integer.