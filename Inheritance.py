## Jan 6
## Inheritance

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

## Class Programmer has all the features that is in Employee class --> Inheritance
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python.")

e1 = Employee("rohan Das", 420)
e1.showDetails()
e2 = Programmer("Harry", 4100)
e2.showDetails()
e2.showLanguage()