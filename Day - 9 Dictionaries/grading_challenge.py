student_score = {   
    "Harry" : 81,
    "Rio" : 78,
    "Harsh" : 67,
    "Khushi" : 89,
    "Turakhia" : 92
}

for key in student_score:
    print(key,":",student_score[key])
    
    if student_score[key] > 90:
        student_score[key] = "Outstanding"
    elif student_score[key] > 80:
        student_score[key] = "Exceeds Expectation"
    elif student_score[key] > 70:
        student_score[key] = "Acceptable"
    else:
        student_score[key] = "Fail"
    
    print(key,":",student_score[key])

