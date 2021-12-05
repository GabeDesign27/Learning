from turtle import Turtle

MOVE_DISTANCE = 20


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move(self):
        """ Moves player forward"""
        self.forward(MOVE_DISTANCE)

    def reset_player(self):
        """Resets player position"""
        self.sety(-280)
