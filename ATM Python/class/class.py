# Class is an object programming

# Object could be A boy or human
#  can jump, human can sing, can eat.

class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model



car1 = Car("Toyota", 2016)
car2 = Car("Benz", 2020)
car3 = Car("Honda", 2019)

print(car1.model)
