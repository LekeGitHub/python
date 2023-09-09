# Class
class Person:
    speech = "Say Something"
    def __int__(self, name):
        # This creates a new instance of out Person
        self.name = name

    def print_conv(self):
        print("P1: This person whose name is "+ self.name + "is speaking something!")
        print("P2: But what is he speaking?")