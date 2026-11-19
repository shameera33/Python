from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name, joining_year):
        self._name = name
        self._joining_year = joining_year

    def calculate_years(self):
        return 2025 - self._joining_year

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"Name: {self._name}, Role: {self.get_role()}, Years: {self.calculate_years()}"


class Customer(User):

    def get_role(self):
        return "Customer"


class Vendor(User):

    def get_role(self):
        return "Vendor"


c1 = Customer("Ravi", 2020)
v1 = Vendor("Anjali", 2018)

print(c1)
print(v1)