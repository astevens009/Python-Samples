print()     # Used to format a space at the start of the program

# Flag for determining if the user would like to enter a nother number
try_again = 'Y'

while (try_again == 'Y' or try_again == "YES"):
    userInput = int(input("\nPlease enter a number and I'll tell you if it's odd or even: "))

    if userInput % 2 == 0:
        print("{} is an even number.\n".format(userInput))
    else:
        print("{} is an odd number.\n".format(userInput))

    try_again = input("\nWould you like to enter another number (Y/N): ").upper()

print()     # Used to format a space at the end of the program