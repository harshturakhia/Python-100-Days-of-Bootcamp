students_score = input("Give students score : ").split()

# To get input in list via for loop
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])

print(f"Given input of students score is : {students_score}")


# print("Direct way of geting maximum is by max() function : ")
# print(max(students_score))


answer = 0

for score in students_score:
    if score > answer:
        answer = score

print(f"Maximum by comparing is : {answer}")
