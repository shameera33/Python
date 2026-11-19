class Account:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __add__(self, other):
        return self._balance + other._balance


class SavingsAccount(Account):

    def calculate_interest(self):
        return self._balance * 0.05


class CurrentAccount(Account):

    def calculate_interest(self):
        return self._balance * 0.02


s1 = SavingsAccount("Ravi", 10000)
c1 = CurrentAccount("Anjali", 15000)

print("Savings Account")
print("Name:", s1._name)
print("Balance:", s1._balance)
print("Interest:", s1.calculate_interest())

print("\nCurrent Account")
print("Name:", c1._name)
print("Balance:", c1._balance)
print("Interest:", c1.calculate_interest())

print("\nTotal Balance:", s1 + c1)