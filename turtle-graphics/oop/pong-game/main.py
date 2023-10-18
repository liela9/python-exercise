from turtle import Screen
from player import Player
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
R_PADDLE_POS = (350, 0)
L_PADDLE_POS = (-350, 0)
R_SCORE_POS = (150, 230)
L_SCORE_POS = (-150, 230)
WALL = 290
PLAYERS_Y_FRONT = 320
PLAYERS_Y_BACK = 340
BALL_DIST = 50 # the ball distance from the middle of the paddle.

screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Game")
screen.tracer(0) # turn the tracer off, for better animation of the game.

r_player = Player(R_PADDLE_POS, R_SCORE_POS) # right player
l_player = Player(L_PADDLE_POS, L_SCORE_POS) # left player

screen.listen()
screen.onkey(r_player.paddle.up, "Up")
screen.onkey(r_player.paddle.down, "Down")
screen.onkey(l_player.paddle.up, "w")
screen.onkey(l_player.paddle.down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(0.03)
    screen.update() # show all the changes on the screen at once.
    ball.move()

    # detect collision with valid wall (top/bottom).
    if ball.ycor() > WALL or ball.ycor() < -WALL:
        ball.bounce_y()

    # detect collision with paddles.
    if ball.xcor() > PLAYERS_Y_FRONT and ball.distance(r_player.paddle) < BALL_DIST or ball.xcor() < -PLAYERS_Y_FRONT and ball.distance(l_player.paddle) < BALL_DIST:
        ball.bounce_x()

    # detect r paddle misses.
    if ball.xcor() > PLAYERS_Y_BACK:
        l_player.score_board.increase_score()
        ball.reset_position()
        time.sleep(0.1)

    # detect l paddle misses.
    if ball.xcor() < -PLAYERS_Y_BACK:
        r_player.score_board.increase_score()
        ball.reset_position()
        time.sleep(0.1)


screen.exitonclick()