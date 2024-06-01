from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(x=randrange(-280, 280), y=randrange(-280, 280))

