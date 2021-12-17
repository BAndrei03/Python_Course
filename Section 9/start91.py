student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for value in student_scores:
    if student_scores[value] > 90:
        student_grades[value]="Outstanding"
    elif student_scores[value] < 91 and student_scores[value]>80:
        student_grades[value]="Exceeds Expectations"
    elif student_scores[value] < 81 and student_scores[value]>70:
        student_grades[value]="Acceptable"
    elif student_scores[value] < 71:
        student_grades[value]="Fail"
# 🚨 Don't change the code below 👇
print(student_grades)


