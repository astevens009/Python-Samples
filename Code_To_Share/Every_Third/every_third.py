#   Author: A. Stevens
#   Date:   6/10/2021
#
#   Description: Print every third character in a string. If the string 
#                len is < 3 print a message
#==========================================================================

# TODO: Have the program continue until the user quits

user_input = input("Please type in a string with 3 or more characters: ")

if len(user_input) < 3:
    print("Not enough charcaters. Please enter a string of 3 or more characters.")
else:
    index = 2
    while index <= (len(user_input) - 1):
        print(user_input[index])
        index += 3