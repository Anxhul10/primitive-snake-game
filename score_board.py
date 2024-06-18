from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score_show()
        self.high_score = 0
        with open("high_score.txt","r") as file:
            self.high_score = int(file.read())

        self.h_score_show()
    def h_score_show(self):
        self.goto(30, 260)
        self.write(arg=f"high score:{self.high_score}", font=('Arial', 18, 'normal'))

    def h_score_update(self):
        if self.high_score < self.Score:
            self.high_score = self.Score
        self.h_score_show()
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))


    def score_show(self):
        self.goto(-90, 260)
        self.write(arg=f"Score:{self.Score}", font=('Arial', 18, 'normal'))


    def score_update(self):
        self.Score += 1
        self.clear()
        self.score_show()
        self.h_score_show()

    def game_over(self):
        # self.goto(-80, 0)
        # self.write(arg=f"Game over", font=('Arial', 35, 'normal'))
        self.h_score_update()
        self.Score = 0
        self.goto(-90, 260)
        self.clear()
        self.score_show()
        self.h_score_show()




