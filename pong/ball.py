from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.cur_x = 0
        self.cur_y = 0
        self.x_rate = 10
        self.y_rate = 10
        self.move_speed = 0.1

    def move(self):
        self.cur_x += self.x_rate
        self.cur_y += self.y_rate
        self.goto(self.cur_x, self.cur_y)

    def bounce_y(self):
        self.y_rate *= -1

    def bounce_x(self):
        self.x_rate *= -1
        self.move_speed = self.move_speed * 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.cur_x = 0
        self.cur_y = 0
        self.move_speed = 0.1
        self.bounce_x()

