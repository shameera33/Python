from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name, account_year):
        self._name = name
        self._account_year = account_year

    def account_age(self):
        return 2025 - self._account_year

    @abstractmethod
    def get_role(self):
        pass


class Admin(User):

    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"Name: {self._name}, Role: {self.get_role()}, Account Age: {self.account_age()} years"


class Guest(User):

    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"Name: {self._name}, Role: {self.get_role()}, Account Age: {self.account_age()} years"


a1 = Admin("Ravi", 2020)
g1 = Guest("Anjali", 2023)

print("Role:", a1.get_role())
print("Account Age:", a1.account_age())
print(a1)

print()

print("Role:", g1.get_role())
print("Account Age:", g1.account_age())
print(g1)