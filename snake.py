from turtle import Turtle
from random import choice
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POS = [0, -20, -40]
color = ["grey",  "white"]


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for cor in POS:
            self.add(cor)

    def add(self, pos):
        t = Turtle(shape="square")
        self.segment.append(t)
        t.color(choice(color))
        t.penup()
        t.goto(x=pos, y=0)

    def extend(self):
        self.add(self.segment[-1].xcor())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(10)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def reset(self):
        for i in self.segment:
            i.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

