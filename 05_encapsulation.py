# Scenario: A bank account protects its balance from direct modification.
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("Neha", 5000)
account.deposit(1500)
account.withdraw(2000)
print("Available balance: Rs.", account.get_balance())
