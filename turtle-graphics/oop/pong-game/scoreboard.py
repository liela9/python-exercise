from turtle import Turtle

FONT = ("Arial", 40, "bold")
ALIGNMENT = "center"
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self, score_pos):
        super().__init__()
        self.score = 0
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(score_pos)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
