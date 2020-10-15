import random

number_of_guesses = 0   # The number of guesses the user has made
guess = -1
upper_limit = 10
# NOTE: The following line will produce a random number between 1 and 10, inclusive
answer = random.randint(1, upper_limit)

# TODO: Comment out the following line after you've completed testing
# print("TEST: answer is: {}".format(answer))

print("Please guess a number between 1 and {}. (Enter 0 to quit): ".format(upper_limit))

while guess != answer and number_of_guesses < 3:
    guess = int(input())
    if guess == answer:
        print("AWESOME! You got it!")
        break
    elif guess == 0:
        print("Good-bye.")
        break
    else:
        if guess > answer:
            print("{0} is too high. Please try again.".format(guess))
            number_of_guesses += 1
        if guess < answer:   # user input is lower than the answer
            print("{0} is too low. Please try again.".format(guess))
            number_of_guesses += 1
 
# Only print the following if the user made 3 guesses
if number_of_guesses >= 3:
    print("Sorry, the correct number was {}".format(answer))

    