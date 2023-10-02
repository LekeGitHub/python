class Car: # Car class is a Car Object Template
    def __init__(self, name="", model="", year="", speedometer=""): # Attribute of the object
        self.name = name
        self.model = model
        self.year = year
        self.speedometer = speedometer

    def move(self):
        print(f"{self.name} drive at the rate of 220 km/h")


def main():
    Toyota = Car("Toyota", "Camery", 2017, 250)
    Toyota.move()




