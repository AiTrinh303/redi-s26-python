from abc import ABC, abstractmethod

class BankAccount(ABC):  # abstract class
    account_counter = 0

    def __init__(self, balance=0.0):
        self._balance = balance
        BankAccount.account_counter += 1

    def __del__(self):
        BankAccount.account_counter -= 1

    @property
    def balance(self):
        return self._balance  

    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Balance must be a number.")
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self._balance += amount        

    @abstractmethod
    def withdraw(self, amount):
        pass  # bắt buộc class con phải override

    def __str__(self):
        return f"{self.__class__.__name__}(balance={self._balance})"
    
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

class CheckingAccount(BankAccount):
    def __init__(self, balance=0.0, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if self._balance - amount < -self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded.")
        self._balance -= amount       

class InvestmentAccount(BankAccount):
    def __init__(self, balance=0.0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate        



acc1 = SavingsAccount(200)
acc2 = CheckingAccount(100, overdraft_limit=50)
acc3 = InvestmentAccount(500, interest_rate=0.1)

acc1.withdraw(50)
print(acc1)  # SavingsAccount(balance=150)

acc2.withdraw(120)
print(acc2)  # CheckingAccount(balance=-20)        

acc3.apply_interest()
print(acc3)  # InvestmentAccount(balance=550.0)