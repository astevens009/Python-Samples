import datetime

def check_birth_date(birth_date):
    # Date will be U.S. format
    month, day, year = birth_date.split('/')

    isValidBirthDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidBirthDate = False

    if not isValidBirthDate:
        print("\n{} is not a valid date. Please enter birth date in the form mm/dd/yyyy.\n".format(birth_date))

    return isValidBirthDate


def checkInfo(fName, lName, DOB, goals):
    # TODO: confirm that the inputs are valid

    # print("TEST: goals.isalpha() = {}".format(goals.isalpha()))

    if fName.isalpha() and lName.isalpha() and goals.isprintable() and check_birth_date(DOB):
        return True
    else:
        if not fName.isalpha():
            print("\nFirst name is not valid. Please enter text.\n")
        if not lName.isalpha():
            print("\nLast name is not valid. Please enter text.\n")
        if not goals.isalpha():
            print("\nGoals input is not valid text.\n")
        return False


def get_bio():
    isValidInfo = False

    while isValidInfo == False:
        # TODO: Prompt user for bio info
        first_name = input("\nPlease enter your first name: ")
        last_name = input("Please enter your last name: ")
        birth_date = input("Please enter your date of birth (mm/dd/yyyy): ")
        goals = input("What are your career goals:\n")

        # TODO: Check that information is valid
        isValidInfo = checkInfo(first_name, last_name, birth_date, goals)

        # Valid inputs should break out of the loop
        if isValidInfo:
            print("\n\nName: {} {}\nDOB: {}\n{}\nGoals:\n{}\n\n"
                  .format(first_name, last_name, birth_date, ("=" * 25), goals))

get_bio()