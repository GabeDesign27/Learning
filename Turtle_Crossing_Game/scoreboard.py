from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = 1

    def write_score(self):
        """Writes score and level for game"""
        self.goto(-200, 280)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 12, "normal"))
        self.goto(200, 280)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 12, "normal"))

    def update_score(self):
        """increments score and level by 1"""
        self.clear()
        self.score += 1
        self.level += 1

    def game_over(self):
        """Displays game over screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
