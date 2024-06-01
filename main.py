from turtle import Screen
from snake import Snake
from FOOD import Food
from score_board import Score

import time
sn = Snake()
s = Screen()
s.tracer(0)
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
position = [0, -20, -40]
s.onkey(fun=sn.up, key="Up")
s.onkey(fun=sn.down, key="Down")
s.onkey(fun=sn.right, key="Right")
s.onkey(fun=sn.left, key="Left")
s.listen()
food = Food()
score = Score()
run = True
while run:
    s.update()
    time.sleep(0.1)
    sn.move()
    if sn.head.xcor() > 290 or sn.head.xcor() < -290 or sn.head.ycor() > 290 or sn.head.ycor() < -290:
        score.game_over()
        sn.reset()

    for seg in sn.segment[1:]:
        if sn.head.distance(seg) < 5:
            score.game_over()
            sn.reset()
    if sn.head.distance(food) < 15:
        food.refresh()
        sn.extend()
        score.inc_score()
        score.new_score()


s.exitonclick()
