friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
import random

# 1st option
has_to_pay = random.choice(friends)
print(f"{has_to_pay}, you have to pay!")

# 2nd option
has_to_pay2 = random.randint(0,4)
print(f"You, {friends[has_to_pay2]}, have to pay!")