# EXAMPLE 1: Function definition and syntax
# def multiply():
#     """Multiplies two literal values, 3.1415 by 21

#     Returns:
#         `float`: The result of multiplying the literal values
#     """
#     result = 3.1415 * 21
#     return result

# answer = multiply()
# print("The result is: {}".format(answer))

# EXAMPLE 2: Function definition using parameters
# def multiply(a, b):
#     """Multiply the arguments passed into this function

#     Args:
#         a (`int`): First integer input by the user
#         b (`int`): Second integer input by the user

#     Returns:
#         `int`: The product of the two integers input by the user
#     """
#     result = a * b
#     return result

# # NOTE: Display the Docstring for the multiply(...) function
# # help(multiply)

# a = int(input("Please enter a number: "))
# b = int(input("Please enter another number: "))

# answer = multiply(a, b)
# print("The result of {} x {} is: {}".format(a, b, answer))

# EXAMPLE 3: Using a function in a loop
# def multiply(a, b):
#     """Multiply the arguments passed into this function

#     Args:
#         a (`int`): First integer input by the user
#         b (`int`): Second integer input by the user

#     Returns:
#         `int`: The product of the two integers input by the user
#     """
#     result = a * b
#     return result

# for num in range(1, 6):
#     product = multiply(2, num)
#     print("{} x {} = {}".format(2, num, product))