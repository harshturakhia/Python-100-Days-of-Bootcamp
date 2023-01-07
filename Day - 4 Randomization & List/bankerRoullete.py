import random

names_string = input("Give everybody names seperated by comma...")
names = names_string.split(",")

print(names)
# length = names.len()
length = len(names)

random_choice = random.randint(0, length-1)
print(random_choice)

print(names[random_choice])
