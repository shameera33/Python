class Person:
    def __init__(self, name, age, **kwargs):
        super().__init__()
        self.name = name
        self.age = age

    def show_details(self):
        print("\nName:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, employee_id, **kwargs):
        super().__init__(**kwargs)
        self.employee_id = employee_id

    def show_details(self):
        super().show_details()
        print("Employee ID:", self.employee_id)


class PartTime(Person):
    def __init__(self, working_hours, **kwargs):
        super().__init__(**kwargs)
        self.working_hours = working_hours

    def show_details(self):
        super().show_details()
        print("Working Hours:", self.working_hours)


class Consultant(Employee, PartTime):
    def __init__(self, project_name, **kwargs):
        super().__init__(**kwargs)
        self.project_name = project_name

    def show_details(self):
        super().show_details()
        print("Project Name:", self.project_name)


p1 = Person(name="Zarah", age=25)

emp = Employee(name="Diya", age=30,
             employee_id="E101")

pt = PartTime(name="Dev", age=22,
              working_hours=5)

ct = Consultant(name="John", age=35,
               employee_id="C101",
               working_hours=5,
               project_name="Website Development")


p1.show_details()
emp.show_details()
pt.show_details()
ct.show_details()
