# set up script wide variables
icecream = ["Chocolate", "Vanilla", "Moose Tracks"]
toppings = ["Cherry", "Sprinkles", "Whip Cream", "Brownie"]
size = ["Small", "Medium", "Large"]

# introduction
print("Welcome to the Icecream Parlor!" "\n" "Please select your base icecream from our menu.")
print("Menu:")

# Iterates through menu and displays choices of icecream
for ice in icecream:
    print(ice)
sel_icecream = input("Icecream choice: ")

# check to ensure that input matches a choice from the menu, if not let customer know
if sel_icecream == icecream[0] or sel_icecream == icecream[1] or sel_icecream == icecream[2]:
    print("Okay, your icecream is " + sel_icecream)
else:
    print("Sorry we don't have that.")

# Iterate through toppings choices from list and display
print("What toppings would you like?\n Toppings:")
for top in toppings:
    print(top)
sel_topping = input("Topping choice: ")

# Check to ensure input is equal to an element from the toppings list (find more efficient way to do this)
if sel_topping == toppings[0] or sel_topping == toppings[1] or sel_topping == toppings[2] or sel_topping == toppings[3]:
    print("You chose " + sel_topping)
else:
    print("sorry we don't have that topping.")

# gme flag variable which sets up while loop
thinking = True
count = 0

# variable count increases while the loop is going, once the count reaches 25, the loop completes
while thinking:
    count = count + 1
    if count >= 25:
        print("I counted to " + str(count) + " all done thinking, goodbye.")
        thinking = False

### debugging
# print(icecream[1])
