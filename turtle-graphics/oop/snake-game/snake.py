from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
SNAKE_FIRST_SIZE = 3
UP = 90
DOWN = 270 
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        """Create the snake."""
        for i in range(SNAKE_FIRST_SIZE):
            self.add_segment(STARTING_POSITION[i]) 

    def add_segment(self, pos):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(pos)
        t.speed("slow")
        self.body.append(t)

    def move(self):
        """Move the snake forward."""

        # the dody follows the head.
        length = len(self.body) - 1
        while length > 0:
            self.body[length].goto(self.body[length - 1].position())
            length -= 1    

        # move the head
        self.head.forward(MOVE_DISTANCE) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:    
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:    
            self.head.setheading(LEFT)

    def eat(self):
        """Extend the snake."""
        self.add_segment(self.body[-1].position())

    def hide_snake(self):
        """Erase the snake from the screen."""
        for segment in self.body:
            segment.hideturtle()

    def reset(self):
        self.hide_snake() 
        self.body.clear() # delete the current snake.
        self.create_snake() # create new snake.
        self.head = self.body[0]
