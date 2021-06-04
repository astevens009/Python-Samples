# Pythagoras Demo
# Author: A. Stevens
# Date: 6/3/2021
# Description: Passing value back from the function (see README file)
#=======================================================================

def is_right_triangle(a, b, c):
    if (a**2 + b**2 == c**2):
        return True
    else:
        return False

side1 = int(input("Please enter the size of side A: "))
side2 = int(input("Please enter the size of side B: "))
side3 = int(input("Please enter the size of side C: "))

if is_right_triangle(side1, side2, side3):
    print("Right-angled")
else:
    print("Not right-angled")