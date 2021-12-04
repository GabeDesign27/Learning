from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.player1_score = 0
        self.player2_score = 0

    def write_score(self, scores):
        self.clear()
        self.write(f"{scores}", align="center", font=("Courier", 80, "normal"))

    def write_winner(self, player):
        self.write(f"Winner: {player}", align="center", font=("Courier", 40, "bold"))
