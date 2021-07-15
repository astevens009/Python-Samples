num1 = 7
num2 = 0

# EXAMPLE 1: Generating an exception

# # Generate an exception
# print(num1 / num2)

# EXAMPLE 2: Using a try/except block
try:
    result = num1 / num2
    print("{} / {} = {}".format(num1, num2, result))
except ZeroDivisionError:
    print("ERROR: Attempting to divide by 0")