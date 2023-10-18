from turtle import Turtle

FIRST_POS = (0, 0)

class Ball(Turtle):

    def __init__(self):
        self.x_move = -10
        self.y_move = 10

        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.reset_position()
        self.move()
        
    def reset_position(self):
        self.goto(FIRST_POS)
        self.bounce_x()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """Change x movement direction."""
        self.x_move *= -1

    def bounce_y(self):
        """Change y movement direction."""
        self.y_move *= -1
