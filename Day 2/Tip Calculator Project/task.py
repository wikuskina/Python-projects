# Exercise to build a tip calculator based on the data provided

print("Welcome to the tip calculator!")
# Asking for a total bill
bill = float(input("What was the total bill? $"))
# Asking for a tip in percentage
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# Asking for the people in total
people = int(input("How many people to split the bill? "))

# Display the total
print(f"this is the total: {bill}")
# Calculate the tip
totalTip = bill*(tip/100)
print(f"this is the total tip: {totalTip}")
tipPerPerson = totalTip/people
print(f"this is the tipe per person: {tipPerPerson}")

# Calculate the result: how much each person pays, bill + tip divided by total ppl
result = (bill + totalTip) / people
print(f"Each person should pay: {result}")
