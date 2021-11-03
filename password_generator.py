#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# # Eazy Level - Order not randomised:
# # e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_let = 0
my_lets = ""
for i in range(0, nr_letters):
    rand_let = random.randint(0, len(letters) - 1)
    my_lets += letters[rand_let]
# debug random letter portion
# print(my_lets)

rand_sym = 0
my_syms = ""
for i in range(0, nr_symbols):
    rand_sym = random.randint(0, len(symbols) - 1)
    my_syms += symbols[rand_sym]
# debug random symbols
# print(my_syms)

rand_num = 0
my_nums = ""
for i in range(0, nr_numbers):
    rand_num = random.randint(0, len(numbers) - 1)
    my_nums += numbers[rand_num]
# debug random numbers
# print(my_nums)

print("-----Easy Password-----\nYour new password is: " + my_lets + my_syms + my_nums)

# Hard Level - Order of characters randomised:
rand_let = 0
my_lets = ""
for i in range(0, nr_letters):
    rand_let = random.randint(0, len(letters) - 1)
    my_lets += letters[rand_let]
# debug random letter portion
# print(my_lets)

rand_sym = 0
my_syms = ""
for i in range(0, nr_symbols):
    rand_sym = random.randint(0, len(symbols) - 1)
    my_syms += symbols[rand_sym]
# debug random symbols
# print(my_syms)

rand_num = 0
my_nums = ""
for i in range(0, nr_numbers):
    rand_num = random.randint(0, len(numbers) - 1)
    my_nums += numbers[rand_num]
# debug random numbers
# print(my_nums)

password = my_lets + my_syms + my_nums
rand_password = ""
for i in range(0, len(password)):
    rand_char = random.randint(0, len(password) - 1)
    rand_password += password[rand_char]

# print(password)
print("-----Hard Password-----\nYour new password is: " + rand_password)

# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
