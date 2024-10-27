# Calculator project
# Choose two numbers and operation to perform
# Continue calculating with previous result or start new calculation
operators = "+ \n - \n * \n / \n"

# getting user input: numbers and operators
first_number = int(input("What's the first number? "))
print(operators)
operation = input("Pick an operation: +, -, * or /")
second_number = int(input("What's the second number? "))
result = 0

def add(n1, n2):
    return n1 + n2

def subtract(m1,m2):
    return m1 - m2

def multiply(p1,p2):
    return p1 * p2

def divide(r1, r2):
    return r1 / r2

if operation == "+":
    result = add(first_number,second_number)

elif operation == "-":
    result = subtract(first_number,second_number)

elif operation == "*":
    result = multiply(first_number, second_number)

elif operation == "/":
    result = divide(first_number, second_number)

print(f"{first_number} {operation} {second_number} = {result}")


