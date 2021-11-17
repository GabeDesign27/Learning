# print logo for game
import art
from game_data import data
import random

play = True
turn = 0
points = 0
decision = ""
my_data = data


# create function for random data selection
def rand_person():
    pick = random.randint(0, len(data) - 1)
    person = (data[pick])
    return person


def description(personality):
    person_descrip = personality['name'] + ", a " + personality['description'] + ", from " + personality['country']
    return person_descrip


# create a function for checking user decision
def result_func(a, b, c):
    global play
    global points
    winner = {}
    if c == 'a':
        c = a
    elif c == 'b':
        c = b
    if a['follower_count'] > b['follower_count']:
        winner = a
    elif a['follower_count'] < b['follower_count']:
        winner = b
    if c['name'] == winner['name']:
        print(f"You are correct, {winner['name']} wins.")
        points += 1
        # placeholder = c
        print(f"Your score is: {points}")
        return winner
    elif c['name'] != winner['name']:
        print(f"You picked {c['name']} the winner was {winner['name']}. You lose")
        print(f"Your final score is: {points}")
        play = False
        return winner


def decision_func():
    global decision
    deciding = True
    options = ["a", "b"]
    while deciding:
        decision = input("Who has more followers? Type 'A' or 'B': ").lower()
        if decision not in options:
            print("Invalid input, try again.")
        else:
            deciding = False


person_a = rand_person()
person_b = rand_person()
while person_a == person_b:
    person_b = rand_person()
# create while loop setup
while play:
    # grab 2 random personalities for comparison and display them
    if turn == 0:
        print(art.logo)
        print(f"Person A: {description(person_a)}")
        print(art.vs)
        print(f"Person B: {description(person_b)}")
        decision_func()
        turn += 1
    result = result_func(person_a, person_b, decision)
    if not play:
        exit(0)
    print(art.logo)
    person_a = person_b
    print(f"Person A: {description(person_a)}")
    person_b = rand_person()
    while person_a == person_b:
        person_b = rand_person()
    print(art.vs)
    print(f"Person B: {description(person_b)}")
    decision_func()

# take user input and compare with data on personalities, assess win/lose

# if win, use winning personality to compare against another
