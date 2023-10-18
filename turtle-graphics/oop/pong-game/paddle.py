from turtle import Turtle

PADDLE_MOVEMENT = 30

class Paddle(Turtle):

    def __init__(self, first_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(first_pos)
        self.shapesize(stretch_wid=5, stretch_len=1)        

    def up(self):
        new_y = self.ycor() + PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - PADDLE_MOVEMENT
        self.goto(self.xcor(), new_y)