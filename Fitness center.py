
class Employee:
    def __init__(self, name, role, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.role = role

    def display(self):
        print(self.name, self.role)


class Trainer(Employee):
    def __init__(self, name, role, specialization, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.specialization = specialization

    def display(self):
        print(self.name, self.role, self.specialization)


class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style, **kwargs):
        super().__init__(name=name, role=role, **kwargs)
        self.yoga_style = yoga_style

    def display(self):
        print(self.name, self.role, self.yoga_style)


class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        super().__init__(
            name=name,
            role=role,
            specialization=specialization,
            yoga_style=yoga_style
        )

    def display(self):
        print(self.name, self.role, self.specialization,self.yoga_style)



emp1 = Employee("Aadhi", "Manager")
trainer1 = Trainer("Arjun", "Trainer", "Weight Training")
yoga1 = YogaInstructor("Anya", "Yoga Instructor", "Hatha Yoga")
multi1 = MultiTrainer("Riya", "Multi Trainer", "Fitness Training", "Vinyasa Yoga")


emp1.display()
trainer1.display()
yoga1.display()
multi1.display()