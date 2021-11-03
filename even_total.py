total_even = 0

# iterate through each number from 1 - 100, then add all even numbers up.
for num in range(1, 101):
    if num % 2 == 0:
        total_even += num

print(f"The total is {total_even}")
