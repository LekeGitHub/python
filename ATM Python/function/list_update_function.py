# A function that update a list

# cities = ["Abuja", "Ibadan", "Lagos", "Maryland"]

mcdonalds_burger = []
count = 0
def store(new_burger):
    mcdonalds_burger.append(new_burger)


def get_new_burger():
    global made_burger
    made_burger = input("Enter new burger made: ")

while count < 10:
    get_new_burger()
    store(made_burger)
    count += 1

print(mcdonalds_burger)