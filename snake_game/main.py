from turtle import Screen
import time
from snake import Snake
from snake_game.food import Food
from score_board import ScoreBoard

# set up screen for snake game
my_screen = Screen()
my_screen.screensize(canvwidth=600, canvheight=600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
# turns animation off so we can call updates instead
my_screen.tracer(0)

# create turtle objects to make initial snake
snake = Snake()
food = Food()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

my_score_board = ScoreBoard()

play = True
while play:
    my_screen.update()
    time.sleep(.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 20:
        food.move_food()
        my_score_board.update_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() <= -370 or snake.head.xcor() >= 370 or snake.head.ycor() <= -370 or snake.head.ycor() >= 370:
        play = False
        my_score_board.game_over()

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) <= 10:
            play = False
            my_score_board.game_over()

# always put this line at the end
my_screen.exitonclick()
