from turtle import Turtle

POSITION1 = (-380, 0)
POSITION2 = (370, 0)
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position1, position2):
        super().__init__()
        self.y_cor = 0
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position1, position2)

    def move_up(self):
        self.y_cor += MOVE_DISTANCE
        self.sety(self.y_cor)

    def move_down(self):
        self.y_cor -= MOVE_DISTANCE
        self.sety(self.y_cor)

    def player_boundaries(self):
        if self.ycor() >= 240:
            self.y_cor = 0
        elif self.ycor() <= - 220:
            self.sety(220)
