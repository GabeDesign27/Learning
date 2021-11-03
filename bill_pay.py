import random

names = input("Please provide a list of names separated by commas: ")
name_list = names.split(",")
count = 0
# debugging to ensure correct list creation
# print(name_list)

for name in name_list:
    count += 1

real_count = count - 1

# verify count iteration
# print(count)
my_int = random.randint(0, real_count)

print("The person responsible for paying the bill is " + name_list[my_int])
