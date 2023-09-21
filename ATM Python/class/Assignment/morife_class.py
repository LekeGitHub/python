class Animal:
    def __init__(self, name, science):
        self.name = name
        self.science = science

animal_1 = Animal("Lion", "Panthera leo")
animal_2 = Animal("Goat", "Capra aegagrus hircus")
animal_3 = Animal("Pig", "Sus scrofa domes")
animal_4 = Animal("Dog", "Canis lupus familiaris")
animal_5 = Animal("Leopard", "Panthera pardus")
animal_6 = Animal("Snake", "Serpentes")
animal_7 = Animal("Deer", "Cervidae")
animal_8 = Animal("Antelope", "Bovidae")


print(animal_1.name, "-", animal_1.science)
print(animal_2.name, "-", animal_2.science)
print(animal_3.name, "-", animal_3.science)
print(animal_4.name, "-", animal_4.science)
print(animal_5.name, "-", animal_5.science)
print(animal_6.name, "-", animal_6.science)
print(animal_7.name, "-", animal_7.science)
print(animal_8.name, "-", animal_8.science)