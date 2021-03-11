import random

# TODO: Create a player class to keep track of who wins

rps_game = {
    1: "rock",
    2: "paper",
    3: "scissors"
}

print("\nLet\'s play \"Rock, Paper, Scissors\":")

for choice in rps_game:
    print("{} for {}".format(choice, rps_game[choice]))

user_choice = int(input("Please make a choice: "))

# print("TEST: You chose {}".format(rps_game[user_choice]))

computer_choice = random.randint(1, 4)

# print("TEST: The computer chose: {}".format(computer_choice))

# TODO: Define which item beats another item

