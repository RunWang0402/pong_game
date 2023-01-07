from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x,y)
        self.Score=0
        self.hideturtle()



    def score(self):
        self.write(f"{self.Score}",False,"center",('Arial',70,'normal'))

    def add_score(self):
        self.clear()
        self.Score+=1
        self.score()

    def game_over_l(self):
        self.goto(0,0)
        self.write("Game Over. The left player won.",False,"center",('Arial',150,'normal'))

    def game_over_r(self):
        self.goto(0, 0)
        self.write("Game Over. The right player won.", False, "center", ('Arial', 150, 'normal'))





