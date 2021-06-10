def get_suffix(num):
    if num >= 11 and num < 20:
        return "th"
    elif num == 1 or num % 10 == 1:
        return "st"
    elif num == 2 or num % 10 == 2:
        return "nd"
    elif num == 3 or num % 10 == 3:
        return "rd"
    else:
        return "th"

def options():
    print("\n1 - With Lower Limit")
    print("2 - Without Lower Limit (starts at 0)")

def display_nums(upper_lim, lower_lim = 0):
    for num in range(lower_lim, upper_lim + 1):
        print("{}{}".format(num, get_suffix(num)))

options()
selection = int(input("\nPlease select and option: "))


if selection == 1:
    lower_limit = int(input("\nPlease enter the lower limit: "))
    upper_limit = int(input("Please enter the upper limit: "))
    display_nums(upper_limit, lower_limit)
else:
    upper_limit = int(input("\nPlease enter the upper limit: "))
    display_nums(upper_limit)
