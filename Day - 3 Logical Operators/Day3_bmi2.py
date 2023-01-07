height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = ((weight) / (height * height))
# print("Your bmi calculation is : ", bmi)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are Under weight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are Normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are Overweight")
elif bmi < 35: 
    print(f"Your bmi is {bmi}, you are Obese")
else:
    print(f"Your bmi is {bmi}, you are Elinically obese")
