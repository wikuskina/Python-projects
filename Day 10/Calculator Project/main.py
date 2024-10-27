# Calculator project
# Choose two numbers and operation to perform
# Continue calculating with previous result or start new calculation
continue_calculate = "N"

# defining functions
# function to collect first, second numbers and operator
def original_info(first_number, second_number, operation):
    return first_number, second_number, operation

# function to collect second number and operation and get the result from previous calc
def secondary_info(result, second_number, operation):
    return first_number, second_number, operation

def calculator(first_number, second_number, operation):
    if operation == "+":
        result = add(first_number, second_number)

    elif operation == "-":
        result = subtract(first_number, second_number)

    elif operation == "*":
        result = multiply(first_number, second_number)

    elif operation == "/":
        result = divide(first_number, second_number)

    print(f"{first_number} {operation} {second_number} = {result}")
    return result

# def operations

def add(n1, n2):
    return n1 + n2

def subtract(m1, m2):
    return m1 - m2

def multiply(p1, p2):
    return p1 * p2

def divide(r1, r2):
    return r1 / r2


while True:
    if continue_calculate == "N":
        first_number = int(input("What's the first number? "))
        second_number = int(input("What's the second number? "))
        operation = input("Pick an operation: +, -, * or /")
        original_info(first_number,second_number,operation)
        calculator(original_info)
        calculation_result = calculator
        continue_calculate = input(
            f"Type Y to continue calculating with {calculation_result}, or N to start a new calculation:  ").upper()
    else:
        first_number = calculator
        print(f"First number is: {first_number}. ")
        second_number = int(input("What's the second number? "))
        operation = input("Pick an operation: +, -, * or /")
        secondary_info(first_number, second_number, operation)
        calculator(secondary_info)
        calculation_result = calculator
        continue_calculate = input(
            f"Type Y to continue calculating with {calculation_result}, or N to start a new calculation:  ").upper()
    
