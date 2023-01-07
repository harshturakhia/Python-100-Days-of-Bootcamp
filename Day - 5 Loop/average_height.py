students_height = input("Give students heights : ").split()

for n in range(0, len(students_height)):
    students_height[n] = int(students_height[n])

print(f"Given input of heights is : {students_height}")

total_height = 0
for height in students_height:
    total_height += height

print(f"Total sum of height is : {total_height}")

no_of_student = 0
for student in students_height:
    no_of_student += 1

print(f"Total number of student is : {no_of_student}")

average_height = round(total_height / no_of_student)
print(f"Average of height is : {average_height}")
