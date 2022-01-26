from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=(FONT, 10, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'Game Over.', align=ALIGNMENT, font=(FONT, 15, 'normal'))