# words to be tested against
test1 = ["T", "R", "U", "E"]
test2 = ["L","O","V","E"]


def calculate_love_score(name1, name2):
    name_to_test = (name1 + name2).upper()

    # final score number1 + number 2
    number1 = 0
    number2 = 0

    for i in name_to_test:
        if i in test1:
            number1 += 1
    print(number1)
    
    for j in name_to_test:
        if j in test2:
            number2 += 1
    print(number2)
    
    convert1 = str(number1)
    convert2 = str(number2)
    convert3 = convert1 + convert2
    final_score = int(convert3)
    
    return final_score

calculate_love_score("Angela Yu", "Jack Bauer")