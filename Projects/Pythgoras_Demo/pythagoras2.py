# Pythagoras Demo
# Author: A. Stevens
# Date: 6/3/2021
# Description: Using the pow() function in the math library (see README file)
#=======================================================================
import math

def is_right_triangle(s1, s2, s3):
    a = math.pow(s1, 2)
    b = math.pow(s2, 2)
    c = math.pow(s3, 2)

    if (a + b == c):
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