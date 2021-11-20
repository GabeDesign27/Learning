MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 250,
    "milk": 500,
    "coffee": 500,
    "money": 0
}

afford = 0


def compare_resource(liquid, storage):
    # create var to access the sub dictionary "ingredients"
    ingredients = liquid["ingredients"]
    check_list = []
    enough_resources = False
    for i in ingredients:
        for x in storage:
            if i == x:
                if ingredients[i] <= storage[x]:
                    # debug to ensure dictionary keys for ingredients accessed
                    # print("There are enough resources.")
                    check_list.append("true")
                else:
                    # debug to ensure dictionary keys for ingredients accessed
                    # print("Not enough resources.")
                    check_list.append("false")
                storage[x] -= ingredients[i]
    # another storage debug
    # print(storage)
    if "false" in check_list:
        return enough_resources
    else:
        enough_resources = True
        return enough_resources


def cash_func(qar, dim, nic, pen, beverage):
    global afford
    value = beverage["cost"]
    cash = {
        "quarter": 25,
        "dime": 10,
        "nickle": 5,
        "penny": 1
    }
    total_change = [qar * cash["quarter"], dim * cash["dime"], nic * cash["nickle"], pen * cash["penny"]]
    total = 0
    for i in total_change:
        total += i
    total = round(total / 100, 3)
    # debug to ensure total properly reached
    # print("total" + str(total))
    afford = round(total - value, 3)
    # debug to ensure math checks out
    # print("afford" + str(afford))
    if afford < 0:
        return False
    else:
        return True


serving = True
will_make = False
# Prompt user by asking “ What would you like?
while serving:
    can_buy = False
    valid = True
    drink_choice = input("What would you like to drink? Espresso/Latte/Cappuccino: ").lower()
    # Print report
    if drink_choice == "report":
        for metric in resources:
            print(metric + ": " + str(resources[metric]))
    if drink_choice == "off":
        serving = False
    # Check resources sufficient for drink of choice, check if the user gives enough money to buy
    is_allowed = False
    if drink_choice in MENU:
        is_allowed = True
        will_make = compare_resource(MENU[drink_choice], resources)
        if will_make:
            # debug to ensure resource subtraction
            # for y in resources:
            #     print(resources[y])
            quarters = int(input("Enter number of quarters: "))
            dimes = int(input("Enter number of dimes: "))
            nickels = int(input("Enter number of nickles: "))
            pennies = int(input("Enter number of pennies: "))
            can_buy = (cash_func(quarters, dimes, nickels, pennies, MENU[drink_choice]))
            add_setup = MENU[drink_choice]
            resources["money"] += add_setup["cost"]
        else:
            print(f"Sorry the machine doesn't have enough resources to create {drink_choice}")
    if not is_allowed and drink_choice != "report":
        if drink_choice != "off":
            print("That is not a valid beverage option, try again.")
    elif is_allowed and can_buy:
        print(f"Thank you for your purchase, your {drink_choice} is dispensing now\nYour change is {afford}")
    elif is_allowed and will_make and not can_buy:
        print("Sorry you did not provide enough change for your selection.")
