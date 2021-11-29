from turtle import Turtle, Screen
import random

screen = Screen()
screen.screensize(canvwidth=500, canvheight=400)
color_list = ["blue", "red", "purple", "green", "yellow", "orange"]
name_list = []
turtles = []


def turtle_maker(colors):
    global name_list
    for num in colors:
        my_turtle = Turtle()
        my_turtle.color(num)
        name_list.append(my_turtle)


def race_setup(t1, t2, t3, t4, t5, t6):
    global turtles
    turtles = [t1, t2, t3, t4, t5, t6]
    my_y = 0
    my_x = -500
    for racer in turtles:
        racer.shape("turtle")
        racer.penup()
        racer.sety(my_y)
        racer.setx(my_x)
        my_y += 40


def race():
    racing = True
    is_first = True
    while racing:
        for racer in turtles:
            if racer.xcor() < 500:
                movement_speed = random.randrange(5, 25)
                racer.forward(movement_speed)
            elif racer.xcor() >= 500 and is_first:
                winner = racer
                is_first = False
            else:
                racing = False
    return winner


# create turtles and assign the turtle instance to variable names
turtle_maker(color_list)
blue = name_list[0]
red = name_list[1]
purple = name_list[2]
green = name_list[3]
yellow = name_list[4]
orange = name_list[5]

bet = screen.textinput(title="Turtle Bet Screen", prompt=f"Which turtle will win? {color_list}: ")
race_setup(blue, red, purple, green, yellow, orange)
who_won = (race())
convert_num = (turtles.index(who_won))
print(f"The winner of the race was {color_list[convert_num]}!")
if bet == color_list[convert_num]:
    print("Congratulations, you bet right!")
else:
    print("Your turtle lost.")

screen.exitonclick()
