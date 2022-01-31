from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as file:
            self.high_score = file.read()
        print(self.high_score)
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score}. High Score: {self.high_score}', align=ALIGNMENT, font=(FONT, 10, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f'Game Over.', align=ALIGNMENT, font=(FONT, 15, 'normal'))