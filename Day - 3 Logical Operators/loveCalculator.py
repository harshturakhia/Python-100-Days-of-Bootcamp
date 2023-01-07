print("Welcome to love calculator...")

boy = input("What is your name : ")
girl = input("What is their name : ")

combined_string = boy + girl
lowerCaseString = combined_string.lower()

t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")

true = t + r + u + e

l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")

love = l + o + v + e

loveScore = str(true) + str(love)

print(loveScore)
