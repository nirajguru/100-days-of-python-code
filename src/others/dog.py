class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self, name):
        print(f"this is {self.name}")

dog = Dog("tommy")
dog.bark("sam") # please note that sam won't be printed
