# Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# function with more than one input
def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"How is it going in {location}")

# positional argument
greet_with("Natalie", "London")

# keyword argument
greet_with(name = "Natalie", location = "London")