print("Welcome to pizza challenge...")
size = input("Which size pizza you want ? S, M, L : ")
pepperoni = input("Do you want to add pepperoni? Y or N : ")
cheese = input("Do you want to add cheese? Y or N : ")
price = 0

if size == 'S':
    price = price + 15

    if pepperoni == 'Y':
        price = price + 2
    else:
        price = price

    if cheese == 'Y':
        price = price + 1
    else:
        price = price

elif size == 'M':
    price = price + 20

    if pepperoni == 'Y':
        price = price + 3
    else:
        price = price

    if cheese == 'Y':
        price = price + 1
    else:
        price = price

else:
    price = price + 25

    if pepperoni == 'Y':
        price = price + 3
    else:
        price = price

    if cheese == 'Y':
        price = price + 1
    else:
        price = price

print(f"Your total bill is {price}$ only")
