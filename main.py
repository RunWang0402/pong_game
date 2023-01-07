from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("PONG")
screen.tracer(0)
game_is_on=True


for number in range(25):
    block=Turtle(shape="square")
    block.penup()
    block.turtlesize(stretch_wid=0.5,stretch_len=0.1)
    block.color("white")
    block.setposition(0,270-number*30)
screen.update() #not sure how this actually works

#make copy from imports
ball=Ball()
score_l=Scoreboard(-50, 200)
score_r=Scoreboard(50,200)
paddle_l=Paddle(-375,250)
paddle_r=Paddle(375,250)
screen.listen()
screen.onkey(paddle_l.move_up,"f")
screen.onkey(paddle_l.move_down,"v")
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")
screen.update()

while game_is_on:
    #time.sleep(0.05)
    ball.move()
    score_l.score()
    score_r.score()
    #detect collision with wall
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.turn_y()
    #detect collision with r_paddle; we want to set up a line of x so we could calculate the distance from it even from the edge
    if ball.distance(paddle_r)<50 and ball.xcor()>367 or ball.distance(paddle_l)<50 and ball.xcor()<-367:
        ball.turn_x()
        ball.increase_speed()
    if ball.xcor()>405:
        ball.reset_position()
        ball.reset_speed()
        score_l.add_score()
    if ball.xcor()<-405:
        ball.reset_speed()
        ball.reset_position()
        score_r.add_score()
    if score_l.Score==10:
        game_is_on=False
        score_l.game_over_l()
    if score_r.Score==10:
        game_is_on=False
        score_r.game_over_r()







    screen.update()
    paddle_r.turn_around()
    paddle_l.turn_around()











screen.exitonclick()