student_scores={
    "Yuvraj":85,
    "Aayush":89,
    "Sujeet":95,
    "Amritesh":88,
}

student_grades={}

for student in student_scores:
    if student_scores[student]>90:
        student_grades[student]="Outstanding"
    elif student_scores[student]>80:
        student_grades[student]="Exceeds Expectation"
    elif student_scores[student]>70:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"      

print(student_grades)              



