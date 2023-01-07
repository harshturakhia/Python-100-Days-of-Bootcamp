import random

print("Welcome to Rock, Paper, Scissor Game...!")

user = input(
    "What will ypu choose ? \nType 0 for Rock, 1 for Paper, 2 for Scissor : ")
computer = random.randint(0, 2)


if user == 0:
    user = 'Rock'
elif user == 1:
    user = 'Paper'
else:
    user = 'Scissor'

if computer == 0:
    computer = 'Rock'
elif computer == 1:
    computer = 'Paper'
else:
    computer = 'Scissor'
# print(user, computer)

print(f"Your choice : {user}")
print(f"Computer choice : {computer}\n")

if user == 'rock' and computer == 'Scissor':
    print("You Win...!")
elif user == 'Paper' and computer == 'rock':
    print("You Win...!")
elif user == 'Scissor' and computer == 'paper':
    print("You Win...!")

elif user == 'Scissor' and computer == 'Scissor':
    print("Match Tied...!")
elif user == 'paper' and computer == 'paper':
    print("Match Tied...!")
elif user == 'rock' and computer == 'rock':
    print("Match Tied...!")

else:
    print("You lose...!")
