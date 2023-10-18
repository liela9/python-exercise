from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_SIZE = 600
SCREEN_EDGE = 295

# set the screen
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turn the tracer off, for better animation of the game.

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = Food()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update() # show all the changes on the screen at once.
    time.sleep(0.1)

    # detect collision of the snake with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.eat()
        score_board.increase_score()

    # detect collision of the snake with itself.
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            print("Fail. You hit your tail.")
            score_board.reset()
            snake.reset()

    # detect collision of the snake with a wall.
    if snake.head.xcor() > SCREEN_EDGE or snake.head.ycor() > SCREEN_EDGE or snake.head.xcor() < -SCREEN_EDGE or snake.head.ycor() < -SCREEN_EDGE:
        print("Fail. You hit a wall.")
        score_board.reset()
        snake.reset()
        
    snake.move()



screen.exitonclick()