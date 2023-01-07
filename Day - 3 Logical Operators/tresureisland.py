print("Welcome to treasure hunt...")

choice1 = input("Where you wanna go? Left or Right : ").lower()

if choice1 == 'left':
    choice2 = input("You want to swim or wait : ").lower()

    if choice2 == 'wait':
        choice3 = input(
            "Which door you want to choose? Red, Yellow, Blue : ").lower()

        if choice3 == 'yellow':
            print("You win!")
        elif choice3 == 'red':
            print("Game over...")
        else:
            print("Game over...")

    else:
        print("Game over...")

else:
    print("Game over...")
