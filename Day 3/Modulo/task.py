# print(10/6)
# print(10%6)
# print(10/3)
# print(10%3) 3 parts divided, 1 left remaining

# checking if number is even or odd with modulo operator
number = int(input("Please input a whole number: "))

if number % 2 == 0 or number == 0:
    print("This number is even")
else:
    print("This number is odd.")