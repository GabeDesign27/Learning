from turtle import Screen
from player import Player
from Turtle_Crossing_Game.cars import Cars
from scoreboard import ScoreBoard
import time

# Set up screen
screen = Screen()
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create game objects
player = Player()
car = Cars()
scoreboard = ScoreBoard()
time_speed = 0.15

# Listen for player input
screen.listen()
screen.onkey(player.move, "w")

# Game loop
play = True
while play:
    screen.update()
    time.sleep(time_speed)
    scoreboard.write_score()

    # Randomize car objects, ensure no more than 20 on screen at a time
    car.randomize()
    if len(car.car_list) < 20:
        car.generate_car()

    # move cars across screen, once the end is reached, delete the car
    car.move_car()
    car.delete_car()

    # Check to see if player made it to end of level, if so, reset player and increment level and scoreboard.
    if player.ycor() >= 290:
        player.reset_player()
        scoreboard.update_score()
        time_speed = time_speed * 0.9

    # Check for player collision with car to enable game over screen
    for cars in car.car_list:
        if player.distance(cars) < 20 and player.xcor() <= cars.xcor() - 15:
            scoreboard.game_over()
            play = False
        elif player.distance(cars) < 20 and player.xcor() <= cars.xcor() + 15:
            scoreboard.game_over()
            play = False

screen.exitonclick()
