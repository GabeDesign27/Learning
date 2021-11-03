import random

my_int = random.randint(0, 10)
my_float = random.random()

# One way to make random floats over 1.0... but always ends up being a factor of 10
print(str(my_int) + str(my_float))

# better way to make random floats (This will make a float between 0 and 10:
print(my_float * 10)
