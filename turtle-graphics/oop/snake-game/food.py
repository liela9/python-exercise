from turtle import Turtle
import random

SCREEN_EDGE = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-SCREEN_EDGE, SCREEN_EDGE)
        rand_y = random.randint(-SCREEN_EDGE, SCREEN_EDGE)
        self.goto(rand_x, rand_y)

    
