import turtle
import paddle
import random

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("cyan")
        self.shapesize(0.7,0.7)
        self.y_move = 5
        self.x_move = 5

    def ball_move(self):
        self.x_new = self.xcor() + self.x_move
        self.y_new = self.ycor() + self.y_move
        self.goto(self.x_new, self.y_new)


    def bounce(self):
        self.y_move *= -1

    def bounce_from_paddle(self):
        self.x_move *= -1
