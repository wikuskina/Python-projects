
# A practical exercise to generate  a simple band name with user input
welcome = "Welcome to the Band Name Generator."
print(welcome)

# user asked for name of their city
question1 = "What's tha name of the city you grew up in?"
print(question1)
input1= input()

# user asked for the name of their pet
question2 = "What's your pet's name?"
print(question2)
input2= input()

# name of the city + name of the pet = name of the band
result= input1 + " " + input2
print("Your band name could be " + result)