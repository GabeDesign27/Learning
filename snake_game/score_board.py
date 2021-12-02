from turtle import Turtle

# always look for hardcoded attributes/variables and bring them here as constants
ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        # self.score_board = Turtle()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.sety(340)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
