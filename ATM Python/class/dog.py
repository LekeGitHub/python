class Dog:
    def __init__(self, name="", height = 0, weight = 0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print(f"{self.name} likes to run")

    def wag_tail(self):
        print(f"{self.name} wags tail alot")

    def barks(self):
        print(f"{self.name} barks all the time!")



Jamal = Dog("Jamal", 30, 15)
Bingo = Dog("Bingo", 70, 25)

Jamal.barks()
Bingo.wag_tail()