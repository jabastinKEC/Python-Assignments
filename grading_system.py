# Case Study 2: Grading System
# Scenario:
# A school needs an automated grading system. Students receive marks in five subjects, and the
# system should determine their overall grade based on an average score.
# Question:
# Write a Python program that:
# 1. Takes marks for five subjects from the user.
# 2. Calculates the average percentage.
# 3. Uses conditional statements (if-elif-else) to determine the grade based on the
# following criteria:
# o 90 and above: A+
# o 80-89: A
# o 70-79: B
# o 60-69: C
# o Below 60: Fail
# 4. Displays the grade.

subjects = ["Java", "Python", "Machine Learning", "Cloud Computing", "DevOps"]
marks = []
total = 0
for i in range(5):
    mark = int(input(f"Enter the {subjects[i]} marks: "))
    marks.append(mark)
    total += mark
avg = total / 5

print("You average is: ",avg)

if(avg >= 90 and avg <= 100):
    print("You got A+ grade!!")
elif(avg >= 80 and avg <= 89):
    print("You got A grade!!")
elif(avg >= 70 and avg <= 79):
    print("You got B grade!!")
elif(avg >= 60 and avg <= 69):
    print("You got C grade!!")
else:
    print("You are fail")