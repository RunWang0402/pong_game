
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,starting_x,starting_y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=0.6,stretch_len=3)
        self.goto(starting_x,starting_y)
        #self.goto(-375,250)
        self.setheading(90)

    def move(self):
        self.forward(10)

    def move_up(self):
        self.move()
        self.setheading(90)

    def move_down(self):
        self.move()
        self.setheading(270)

    def turn_around(self):
        if self.ycor()>250:
            self.move_down()
        elif self.ycor()<-250:
            self.move_up()




