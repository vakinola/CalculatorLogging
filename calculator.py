from functions import *
from logging import print_logger
from datetime import datetime

# This list are the operators allowed to be used in this program
allowed_operators = ["+", "-", "/", "*"]

# This list will be populated with the operations inputed during runtime
operation_functions = []


def check_digit(value_to_check: str) -> bool:
    # This function checks if the input values are digits and when true continues else program is exited

    if value_to_check.isdigit():
        return True
    else:
        print("Please enter only a digit")
        print_logger(1, "Please enter only a digit", datetime.now())
        exit()


def check_operator(operator_to_check: str) -> bool:
    # This function checks if the operators inputed are the ones allowed
    # It then, appends the inputed operators from the user into the "operation_functions" list

    result_of_operator_check = operator_to_check not in allowed_operators

    if result_of_operator_check:
        print("Please choose an operation from the list of approved operators")
        print_logger(
            1, "Please choose an operation from the list of approved operators", datetime.now())
    else:
        if operator_to_check == "+":
            operation_functions.append("addition")
        elif operator_to_check == "-":
            operation_functions.append("subtract")
        elif operator_to_check == "*":
            operation_functions.append("multiply")
        elif operator_to_check == "/":
            operation_functions.append("divide")


def bodmas(position: int, new_list: list, action: str) -> list:
    # position is the index of the operator to be used in performing precedence calculation (BODMAS)
    # new_list is a list which contains the integers inputed at run time
    # action is function to be called based on BODMAS

    first_value = new_list[position]
    second_value = new_list[position+1]
    result = action(first_value, second_value)

    if position == 0:
        new_list.pop(0)
        new_list.pop(0)
        new_list.insert(0, result)
    else:
        new_list.pop(1)
        new_list.pop(1)
        new_list.insert(1, result)

    return new_list


def perform_action(a: str, b: str, c: str) -> list:

    new_list = [int(a), int(b), int(c)]

    if len(new_list) == 3:

        if "multiply" in operation_functions:
            position = operation_functions.index("multiply")
            new_list = bodmas(position, new_list, action=multiply)
            print(new_list)

        elif "divide" in operation_functions:
            position = operation_functions.index("divide")
            new_list = bodmas(position, new_list, action=divide)
            print(new_list)

        elif "addition" in operation_functions:
            position = operation_functions.index("addition")
            new_list = bodmas(position, new_list, action=add)
            print(new_list)

        elif "subtract" in operation_functions:
            position = operation_functions.index("subtract")
            new_list = bodmas(position, new_list, action=subtract)

        operation_functions.pop(position)
        print(operation_functions)

    if "multiply" in operation_functions:

        Result = multiply(new_list[0], new_list[1])
        print(Result)
        print_logger(
            1, f"Result of calculation is {Result}", datetime.now())

    elif "divide" in operation_functions:
        Result = divide(new_list[0], new_list[1])
        print(Result)
        print_logger(
            1, f"Result of calculation is {Result}", datetime.now())

    elif "addition" in operation_functions:
        Result = add(new_list[0], new_list[1])
        print(Result)
        print_logger(
            1, f"Result of calculation is {Result}", datetime.now())

    elif "subtract" in operation_functions:
        Result = subtract(new_list[0], new_list[1])
        print(Result)
        print_logger(
            1, f"Result of calculation is {Result}", datetime.now())

    else:
        Result = "Error occurred in calculation"
        print_logger(
            1, f"{Result}", datetime.now())

    operation_functions.pop()

    return Result


if __name__ == "__main__":

    print("Here is the list of allowed operations")
    print("--------------------")
    print(' "+" for Addition')
    print(' "-" for Subtraction')
    print(' "*" for Multiplication')
    print(' "/" for Division')
    print("--------------------")

    a = input("Enter First value: ")
    check_digit(a)

    operator1 = input("choose operation sign ")
    check_operator(operator1)

    b = input("Enter Second value: ")
    check_digit(b)

    operator2 = input("choose operation sign ")
    check_operator(operator2)

    c = input("Enter Third value: ")
    check_digit(c)

    result = perform_action(a, b, c)
    print(f"The result of {a} {operator1} {b} {operator2} {c} = {result}  ")

    print_logger(
        1, f"The result of {a} {operator1} {b} {operator2} {c} = {result}  ", datetime.now())
