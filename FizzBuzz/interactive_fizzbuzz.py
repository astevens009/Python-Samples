# CHALLENGE: Write a function that returns the next answer int the game of fizz buzz. The user and the computer will count in turn. 
# If the next number is divisible by 3 print "fizz". 
# If the next number is divisible bt 5 print "buzz". 
# If the next number is divisible by both 3 and 5 print "fizz buzz"

def fizz_buzz(num: int):
    """Determine if a number is divisible by 3 or 5 or both

    Args:
        num (int): The number to check

    Returns:
        str: "fizz" if number is divisible by 3; "buzz" if number is divisible by 5; "fizzbuzz" if number is divisible by both; the number if neither condition is true
    """
    if (num % 3 == 0 and num % 5 == 0):
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return str(num)

upper_limit = int(input("Please enter the max number to count: "))

for count in range(1, (upper_limit + 1)):
    # print("TEST: {} : {}".format(fizz_buzz(count), type(fizz_buzz(count))))
    print(fizz_buzz(count))