# Exercise: Factorial Function - (see the README.md file)

def factorial(factorial_number: int):
    """Compute the factorial of the given number

    Args:
        factorial_number (int): Number to compute the factorial of

    Returns:
        int: The factorial of the passed in number
    """
    result = 1

    if factorial_number == 0:
        return result
    else:
        for num in range(1, factorial_number + 1):
            result *= num
        return result

name = input("Please enter your name: ")
print("Hello, {}. I will compute the factorial of any number you give me: ".format(name))
num = int(input("Please enter a number: "))

print("{} factorial is: {}".format(num, factorial(num)))
print()