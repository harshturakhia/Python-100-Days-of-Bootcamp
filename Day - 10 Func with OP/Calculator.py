from art import logo


def calculator():
    print(logo)

calculator()

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


num1 = float(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
should_continue = True

# if should_continue == true then only it goes into this while loop
while (should_continue):

    operation_symbol = input("Pick an operation: ")

    num2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]

    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
        num1 = answer
    else:
        should_continue = False
        calculator()

calculator()
