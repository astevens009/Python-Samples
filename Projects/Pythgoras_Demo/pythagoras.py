# Pythagoras Demo
# Author: A. Stevens
# Date: 6/3/2021
# Description: Printing message from the function (see README file)
#=======================================================================

def is_right_triangle(a, b, c):
    if (a**2 + b**2 == c**2):
        print("Right-angled")
    else:
        print("Not right-angled")

side1 = int(input("Please enter the size of side A: "))
side2 = int(input("Please enter the size of side B: "))
side3 = int(input("Please enter the size of side C: "))

is_right_triangle(side1, side2, side3)