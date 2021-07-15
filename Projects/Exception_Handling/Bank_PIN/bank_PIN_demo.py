#===================================================================
#
#   AUTHOR: A. Stevens
#   DATE:   7.14.2021
#   DESCRIPTION: See README.md for details
#   NOTE:   The code that follows was accepted on the SoloLearn site
#
#===================================================================

try:
    pin = int(input())
    print("PIN code is created")

except ValueError:
	print("Please enter a number")