from turtle import Screen
from paddle import Paddle
from pong.ball import Ball
from scoreboard import Scoreboard
import time

# set up screen
screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# create player paddle
player1 = Paddle(-370, 0)
player2 = Paddle(370, 0)
ball = Ball()
score1 = Scoreboard((-150, 220))
score2 = Scoreboard((150, 220))
scorewin = Scoreboard((0, 0))
score1.write_score(score1.player1_score)
score2.write_score(score2.player2_score)

# listen for user input and execute movement
screen.listen()
screen.onkey(player1.move_up, "Up")
screen.onkey(player1.move_down, "Down")
screen.onkey(player2.move_up, "w")
screen.onkey(player2.move_down, "s")

playing = True
while playing:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # If ball hits top or bottom of screen bounce it off
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # If ball touches paddle, bounce it in opposite direction
    if ball.xcor() >= 360 and ball.distance(player2) <= 50 or ball.xcor() <= -360 and ball.distance(player1) <= 50:
        ball.bounce_x()

    '''If ball goes out of bounds on left or right of screen reset ball and move in opposite direction. Then implements
    scoring to give points to players. Finally, quits game of max score is reached.'''
    if ball.xcor() > 400:
        score1.player1_score += 1
        score1.write_score(score1.player1_score)
        ball.reset_position()
    elif ball.xcor() < -400:
        score2.player2_score += 1
        score2.write_score(score2.player2_score)
        ball.reset_position()

    if score1.player1_score == 10 or score2.player2_score == 10:
        if score1.player1_score > score2.player2_score:
            winner = "Player 1"
        elif score2.player2_score > score1.player1_score:
            winner = "Player 2"
        scorewin.write_winner(winner)
        playing = False


screen.exitonclick()
