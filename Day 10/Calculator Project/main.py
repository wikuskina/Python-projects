# Calculator project
# Choose two numbers and operation to perform
# Continue calculating with previous result or start new calculation

# Function to calculate numbers
def calculator(first_number, second_number, operation):
    if operation == "+":
        result = add(first_number, second_number)
        return result

    elif operation == "-":
        result = subtract(first_number, second_number)
        return result

    elif operation == "*":
        result = multiply(first_number, second_number)
        return result

    elif operation == "/":
        result = divide(first_number, second_number)
        return result

# Operations to be used in calculator function

def add(n1, n2):
    return n1 + n2

def subtract(m1, m2):
    return m1 - m2

def multiply(p1, p2):
    return p1 * p2

def divide(r1, r2):
    return r1 / r2


# Calculator main function that runs at the beginning of the program
# It asks for 1st number (once, if operations continues with following result)
# Or again, if user resets the results and calculates from the beginning
def calculator_main():
    continue_calculate = "Y"
    first_number = float(input("What's the first number? "))

    while continue_calculate == "Y":
        second_number = float(input("What's the second number? "))
        operation = input("Pick an operation: +, -, * or /")

        # Storing calculation result that can be re-used
        calculation_result = calculator(first_number, second_number, operation)
        print(f"{first_number} {operation} {second_number} = {calculation_result}")
        
        # Asking user if they want to continue with the same number or start from the beginning
        continue_calculate = input(
        f"Type Y to continue calculating with {calculation_result}, or N to start a new calculation:  ").upper()

        # If they want to continue, they already have the first number
        # If not - the main functions runs again and asks for the first number (input)
        if continue_calculate == "Y":
            first_number = calculation_result
        else:
            continue_calculate = "N"
            print("\n"*25)
            calculator_main()


calculator_main()


