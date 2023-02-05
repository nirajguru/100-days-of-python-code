class Employee:
    def __init__(self, name):
        self.name = name

    def displayEmployeeDetails(self):
        print(self.name)

emp1 = Employee("niraj")
emp1.displayEmployeeDetails()

emp2 = Employee("matthew")
emp2.displayEmployeeDetails()


