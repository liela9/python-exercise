from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

# a bet pop up.
user_bet = screen.textinput(title="Make a bet", prompt="Wich turtle will win the race? Enter a color.")

turtles = []
colors = ["red", "blue", "green", "yellow", "purple"]
start_y_coordinate = 125

# set turtles to the starting positions.
for i in range(5):
    new_turtle = Turtle(shape="turtle")
    turtles.append(new_turtle)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_y_coordinate)
    start_y_coordinate -= 50

speeds = [0, 10, 6, 3, 1] # [fastest, fast, normal, slow, slowest]
race_on = True
race_end_point = 230

# start the race. stop when the first turtle gets to the end point.
while race_on:
    for i in range(5):
        turtles[i].speed(random.choice(speeds))
        turtles[i].forward(random.randint(5, 20))
        if turtles[i].xcor() > race_end_point:
            race_on = False
            winner = turtles[i]
            break

if winner.pencolor() == user_bet:
    print(f"\nYou got it! The {user_bet} turtle won the race.")
else:
    print(f"\nYou lose. The {winner.pencolor()} turtle won the race.")

screen.exitonclick()