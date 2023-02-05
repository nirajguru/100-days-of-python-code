class Vehicle:
    num_of_wheels = 2
    def is_electric(self):
        return True

class Car(Vehicle):
    def __init__(self):
        print(self.num_of_wheels)

car = Car()
print(car.is_electric())