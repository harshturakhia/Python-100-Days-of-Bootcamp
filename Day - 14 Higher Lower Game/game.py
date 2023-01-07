from art import logo
from game_data import data

import random

# Display art
print(logo)

score = 0

# Generate random account from game data
user1 = random.choice(data)
user2 = random.choice(data)

if user1 == user2:
    user2 = random.choice(data)

# Format to printable way


def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, {account_description}, from {account_country}"


print(f"Compare A : {format_data(user1)}")
print(f"Against B : {format_data(user2)}")

# Ask user for choice
guess = input(" Who has more follower ? Type A or B : ").lower()

user1_follower = user1["follower_count"]
user2_follower = user2["follower_count"]

# Compare follower


def check_answer(guess, user1_follower, user2_follower):
    if user1_follower > user2_follower:
        return guess == "a"
    else:
        return guess == "b"


is_correct = check_answer(guess, user1_follower, user2_follower)

# User feedback
if is_correct:
    score = score + 1
    print(f"You are right! Current score : {score}")

else:
    print(f"You are wrong! Final score : {score}")

# Keep score
