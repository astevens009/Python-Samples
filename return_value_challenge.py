# CHALLENEGE:
#   Modify the get_integer() function so that it prints a message,
#   if the user enters an invalid number

import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)    # breaks out of the loop
        # else:
        if temp.isspace():
            print("Blank input not permitted. Please enter a number.")
        else: 
            print("\"{}\" is invalid. Please enter a number"
                .format(temp))


upper_limit = 10
# NOTE: The following line will produce a random number between 1 and 10, inclusive
answer = random.randint(1, upper_limit)

# TODO: Comment out the following line after you've completed testing
print("TEST: answer is: {}".format(answer))

print("Please guess a number between 1 and {}: ".format(upper_limit))
# guess = int(input())
guess = get_integer("Enter input here: ")

if guess == answer:
    print("AWESOME! You got it the first time!")
else:   # the guess was incorrect
    if guess > answer:
        print("{0} is too high. Please try again.".format(guess))
    else:   # user input is lower than the answer
        print("{0} is too low. Please try again.".format(guess))
    # guess = int(input())
    guess = get_integer("Enter input here: ")
    if guess == answer:
        print("Huzzah! You got it right!")
    else:
        print("Sorry, {0} is not the correct answer.".format(guess))
