student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
#print(range(1, 10))

# total score of all scores using python max function
total_exam_score = sum(student_scores)
print(f"Sum of all scores using sum function: {total_exam_score}")

# total score of all scores using for loop
sum = 0
for score in student_scores:
    sum = score + sum
print(f"Sum of all scores using for loop: {sum}")

# biggest score of all scores using python max function
max_score = max(student_scores)
print(f"Larges score calculated using max functon: {max_score}")

# biggest score of all scores using for loop
maximum_score = 0
for score in student_scores:
    if maximum_score < score:
        maximum_score = score
        # print(f"this is maximum score {maximum_score} and current{score}")

print(f"Largest score calculated using for loop: {maximum_score}")


