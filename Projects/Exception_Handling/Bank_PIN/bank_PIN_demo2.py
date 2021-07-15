#===================================================================
#
#   AUTHOR: A. Stevens
#   DATE:   7.14.2021
#   DESCRIPTION: See README.md for details
#   NOTE:   Modified code to display a prompt to the user
#
#===================================================================

try:
    pin = int(input("Please type in your PIN: "))
    print("PIN code is created")

except ValueError:
	print("Please enter a number")