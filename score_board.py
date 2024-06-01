from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("hi_scr.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=280)
        self.new_score()

    def inc_score(self):
        self.score += 1

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("../../OneDrive/Desktop/hi_scr.txt", mode="w")as hs:
                high_scr = str(self.high_score)
                hs.write(high_scr)
        self.score = 0
        self.new_score()

    def new_score(self):
        self.clear()

        self.write(arg=f"SCORE:{self.score} High_Score:{self.high_score}", align="center", font=('Fantasy', 14, 'bold'))


