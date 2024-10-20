# take two names and compare them against words TRUE LOVE and calculate how many times they match
# each number that matches turned to string and then concacenated
# then turn the number into integer, e.g. 3+ 5 = 35 and this would be the score for specific names


# words to be tested against
test1 = ["T", "R", "U", "E"]
test2 = ["L", "O", "V", "E"]

def calculate_love_score(name1, name2):
    name_to_test = (name1 + name2).upper()

    # final score number1 + number 2
    number1 = 0
    number2 = 0


    for i in name_to_test:
        if i in test1:
            number1 += 1
    #print(number1)

    for j in name_to_test:
        if j in test2:
            number2 += 1
    #print(number2)


    score = str(number1)+str(number2)
    #print(score)
    final_score = int(score)
    
    print(f"This is your couple score: {final_score}")

    return final_score



calculate_love_score("Catniss Everdeen", "Peeta Mellark")
