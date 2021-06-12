#   Author: A. Stevens
#   Date:   6/10/2021
#
#   Description: Print every third character in a string. If the string 
#                len is < 3 print a message
#==========================================================================

# Print intro message
print("""

Every Third: Prompts for a string then prints every 3rd character. If the string has less than 3 characters it reports this

  To exit just type '.exit' 

""")

while True:

    s = input("Please enter a string with 3 or more characters: ")

    if s == ".exit":
        print("\n Good-bye! \n")
        break

    if len(s) < 3:
        print("'{}' has less than 3 characters. \n".format(s))
        continue 

    lst = list(s)
    print('Result: {}\n'.format(lst[2::3]))
