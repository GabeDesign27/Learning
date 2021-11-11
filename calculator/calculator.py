from art import logo


# Adding
def add(num1, num2):
    return num1 + num2


# Subtraction
def subtract(num1, num2):
    return num1 - num2


# Multiply
def multiply(num1, num2):
    return num1 * num2


# Division
def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
count = 0
answer = 0
print(logo)
num1 = float(input("Please enter a number: "))

isplay = True
while isplay:
    operator_list = []
    operator_string = ""

    for op in operations:
        operator_list.append(op)
    for i in operator_list:
        operator_string += i
    print(operator_string)
    math = input("Choose an operation from the line above: ")
    num = float(input("Enter a number: "))

    calculation = operations[math]
    if count == 0:
        answer = calculation(num1, num)
    else:
        answer = calculation(answer, num)
    count += 1

    play = input(f"Would you like to keep calculating with {answer}? y/n: ")
    if play == "y":
        isplay = True
    elif play == "n":
        isplay = False
    else:
        isplay = False
