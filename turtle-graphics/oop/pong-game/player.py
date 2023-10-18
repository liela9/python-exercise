from paddle import Paddle
from scoreboard import Scoreboard

class Player():

    def __init__(self, paddle_pos, score_pos):
        self.paddle = Paddle(paddle_pos)
        self.score_board = Scoreboard(score_pos)
