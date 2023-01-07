from turtle import Turtle
import random
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=0.55,stretch_len=0.55)
        self.y_move=1.5
        self.x_move=1.5
        self.move_speed = 0.9

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x, new_y)


    def turn_y(self):
        self.y_move*=-1#this is good to know
        #self.move_speed*=0.9

    def turn_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.turn_x()
        self.move_speed=0.9

    def increase_speed(self):
        self.y_move*=1.5
        self.x_move*=1.5

    def reset_speed(self):
        self.y_move/=self.y_move
        self.x_move /= self.x_move



    #def


