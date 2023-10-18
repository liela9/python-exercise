from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"
SCREEN_EDGE = 270

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake-game/scorehistory.txt", mode="r") as file:
            self.max_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=SCREEN_EDGE)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Max Score: {self.max_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.max_score:
            self.max_score = self.score
            with open("snake-game/scorehistory.txt", mode="w") as file:
                file.write(f"{self.max_score}") # save the max score in "scorehistory.txt" for next games.
        self.score = 0
        self.update_scoreboard()