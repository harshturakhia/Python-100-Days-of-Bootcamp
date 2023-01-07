import math 

height = int(input("Height of wall : "))
width = int(input("Width of wall : "))

coverage = 5

def calc(height, width, coverage):
    no_of_can = int( (height * width)/(coverage) ) 
    no_of_can = math.ceil(no_of_can)
    print(f"You will need {no_of_can} cans")

calc(height, width, coverage)