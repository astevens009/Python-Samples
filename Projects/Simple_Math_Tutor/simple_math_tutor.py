from multipledispatch import dispatch
import random

def displayMenu():
    menu = {
        'A' : "Addition",
        'S' : "Subtraction",
        'M' : "Multiplication",
        'D' : "Division",
        'X' : "Exit"
        }
    
    for option in menu:
        print("{} - {}".format(option, menu[option]))
        
        
def numbers_option():
    print("\nWould you like to enter the numbers for computation or have them automatically generated?\n")
    
    num_menu = {
        'I' : "I will input the numbers",
        'G' : "Please generate numbers for computation"
    }
    
    for option in num_menu:
        print("{} - {}".format(option, num_menu[option]))
    
    option = input("\nEnter selection here: ")
    return option


def get_numbers():
    """
    Prompt the user for the numbers that they want to perform the selected operation on
    The input will be stored in a list which will then be returned as a tuple
    """
    
    num_list = []
    # TODO: Modify this to allow the user to determine how many numbers to input
    for count in range(2):
        if count == 0:
            print("Please enter the first number: ")
        else:
            print("Please enter the next number: ")

        num_list.append(int(input()))
        
    return tuple(num_list)



@dispatch(str, tuple)
def generate_problem(operation, operands):
    # print("\nTEST:\nOperation: {}\nOperands: {}\n".format(operation, operands))
    tries = 1
    while True:
        if operation == 'A':
            sum = int(operands[0]) + int(operands[1])
            print("{} + {} = ?".format(operands[0], operands[1]))
            userInput = int(input("Enter your answer here: "))
            if userInput == sum:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you add {} to it the result will be {}.\n".format(operands[0], operands[1], sum))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'S':
            diff = int(operands[0]) - int(operands[1])
            print("{} - {} = ?".format(operands[0], operands[1]))
            userInput = int(input("Enter your answer here: "))
            if userInput == diff:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you remove {} from it the result will be {}.\n".format(operands[0], operands[1], diff))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'M':
            prod = int(operands[0]) * int(operands[1])
            print("{} x {} = ?".format(operands[0], operands[1]))
            userInput = int(input("Enter your answer here: "))
            if userInput == prod:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you multiply it by {} the result will be {}.\n".format(operands[0], operands[1], diff))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'D':
            if operands[1] == 0:
                print("\nERROR: Division by 0 is not allowed.\n")
                break
            else:
                # quot = float(operands[0]) / float(operands[1])
                quot = operands[0] / operands[1]
                print("{} / {} = ?".format(operands[0], operands[1]))
                userInput = float(input("Enter your answer here: "))
                if userInput == quot:
                    print("\nYOU GOT IT!!\n")
                    break
                else:
                    if tries == 3:
                        print("\nNo. If you have {} of something and you divide it by {} the result will be {}.\n".format(operands[0], operands[1], quot))
                        break
                    else:
                        print("\nNot quite. Try again...\n")
                        tries += 1
        
      

def generate_operand():
    return random.randint(1, 100)



@dispatch(str)
def generate_problem(operation):
    # print("\nTEST:\nOperation: {}\n".format(operation))
    tries = 1
    operand1 = generate_operand()
    operand2 = generate_operand()
    
    while True:
        if operation == 'A':
            sum = int(operand1) + int(operand2)
            print("{} + {} = ?".format(operand1, operand2))
            userInput = int(input("Enter your answer here: "))
            if userInput == sum:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you add {} to it the result will be {}.\n".format(operand1, operand2, sum))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'S':
            diff = int(operand1) - int(operand2)
            print("{} - {} = ?".format(operand1, operand2))
            userInput = int(input("Enter your answer here: "))
            if userInput == diff:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you remove {} from it the result will be {}.\n".format(operand1, operand2, diff))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'M':
            prod = int(operand1) * int(operand2)
            print("{} x {} = ?".format(operand1, operand2))
            userInput = int(input("Enter your answer here: "))
            if userInput == prod:
                print("\nYOU GOT IT!!\n")
                break
            else:
                if tries == 3:
                    print("\nNo. If you have {} of something and you multiply it by {} the result will be {}.\n".format(operand1, operand2, diff))
                    break
                else:
                    print("\nNot quite. Try again...\n")
                    tries += 1
        if operation == 'D':
            if operand2 == 0:
                print("\nERROR: Division by 0 is not allowed.\n")
                break
            else:
                # quot = float(operands[0]) / float(operands[1])
                quot = operand1 / operand2
                print("{} / {} = ?".format(operand1, operand2))
                userInput = float(input("Enter your answer here: "))
                if userInput == quot:
                    print("\nYOU GOT IT!!\n")
                    break
                else:
                    if tries == 3:
                        print("\nNo. If you have {} of something and you divide it by {} the result will be {}.\n".format(operand1, operand2, quot))
                        break
                    else:
                        print("\nNot quite. Try again...\n")
                        tries += 1


def selection_tester(selection):
    if selection == 'A':
        print("You chose Addition...\n")
    elif selection == 'S':
        print("You chose Subtraction...\n")
    elif selection == 'M':
        print("You chose Multiplication...\n")
    elif selection == 'D':
        print("You chose Division...\n")
    elif selection == 'I':
        print("You chose to input the numbers yourself\n")
    elif selection == 'G':
        print("You chose to have the system generate the numbers\n")
    elif selection == 'X':
        print("\nGood-bye...\n")
    else:
        print("Invalid input...\n")


if __name__ == "__main__":
    print("\nWelcome To the Basic Math Tutor\nPlease make a selection:\n")
    
    while True:
        displayMenu()
        selection = input("\nPlease enter your choice here: ")
        
        if selection.capitalize() == 'X':
            # selection_tester(selection.capitalize())
            break
        else:
            # NOTE: Prompt the whether the user wants to enter numbers to have them randomly generated
            numbers_opt = numbers_option()

            if numbers_opt.capitalize() == 'I':
                generate_problem(selection.capitalize(), get_numbers())
            else:
                generate_problem(selection.capitalize())
                break
                
            # selection_tester(numbers_opt.capitalize())
