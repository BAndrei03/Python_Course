student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆


student_grades = {}
for students in student_scores:
    if student_scores[students] > 90:
        student_grades[students] = "Outstanding"
    elif 91 > student_scores[students] > 80:
        student_grades[students] = "Exceeds Expectations"
    elif 81 > student_scores[students] > 70:
        student_grades[students] = "Acceptable"
    elif 71 > student_scores[students]:
        student_grades[students] = "Fail"




# 🚨 Don't change the code below 👇
print(student_grades)