
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock, Paper or Scissors or Q to quit: ").lower()
    if user_wins == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)

