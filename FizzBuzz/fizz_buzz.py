# CHALLENGE: Count numbers from 1 to n and print "fizz" if the number is divisible by 2, or "buzz" if the number is divisible by 5.

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