# Challenge: Modify line 25 in the GuessGame program so that the condition is if "guess == answer"

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("AWESOME! You got it the first time!")
else:   # the guess was incorrect
    if guess > answer:
        print("{0} is too high. Please try again.".format(guess))
    else:   # user input is lower than the answer
        print("{0} is too low. Please try again.".format(guess))
    guess = int(input())
    if guess == answer:
        print("Huzzah! You got it right!")
    else:
        print("Sorry, {0} is not the correct answer.".format(guess))
    