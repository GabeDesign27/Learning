print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

start = input("Please type 'start' to start:\n")
char_race = ["Human", "Elf", "Lizard-men", "Turtle-men"]

if start.lower() == "start":
    print("And so the adventure begins...\nPlease select your character from the following options:")
    for race in char_race:
        print(race)
else:
    exit(1)

sel_race = input("Race: ")

if sel_race.capitalize() in char_race:
    print(f"Your chosen race is {sel_race}.")
else:
    print("That is not a race option, exiting.")
    exit(1)

print("Next lets give your character a name.")

name = input("I'm called: ")

print(
    f"{name} of the {sel_race} race, you have traveled long and far from\n your home. The trip has been tiresome, but your true test is just now beginning.\n")

print("---------\nChapter 1\n----------\n")
decision1 = input("You arrive at a fork in the road. To your left there\nis a dark gloomy dirt road leading into a an eerily quiet forest. To your right\nthere is an overgrown field of corn. No path can be seen, but the\ncorn can't possibly go on for as long as the forest right?\n Which path will you take, left or right? ")

if decision1.lower() == "left":
    print("You hesitantly step onto the forest path, trudging your way into the foreboding darkness.\nYou walk for a short while until you come upon a bend in the path.\nYou hear an ominous call coming from something around the bend, but you can't quiet make out what it is.")
    decision2A = input("After hearing the mysterious call you have two options:\n1. Charge around the bend and face whatever the source is\n2. sneak off the path and scout the area to get a better look. Which do you choose? (1 or 2): ")
    if decision2A == "1":
        print("You charge forward and encounter a large pumpkin in the middle of the path. It rattles around violently, something is inside.\n You bravely extend a hand forward and pick it up. You find a badger inside. The badger looks up at you and then sprints\n away as fast as it can.")
    elif decision2A == "2":
        print("You take caution and get off the path. You crawl between the trees until you feel you are close enough to\nget a glimpse at the source of the sound. As soon as you are about to peak, a gint vine wraps around your leg. You panic and its grip tightens.\n it pulls hard on your leg and drags you into a deep pit of acid.")
        print("--------- GAME OVER ----------")
elif decision1.lower() == "right":
    print("You step forward into the corn. Each stalk towers over you, impairing your field of view.\n crows caw and flap their wings overhead, and a soft breeze begins to pick up as you get further into the field.")
else:
    print("That option is not valid.")
    exit(1)




