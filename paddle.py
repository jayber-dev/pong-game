import turtle
import ball

screen = turtle.Screen()


class Paddle():
    def __init__(self, paddle_position):
        self.paddle = turtle.Turtle()
        self.paddle.penup()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(5,1)
        self.paddle.setposition(paddle_position)

    def moves(self, up_key, down_key):
        def move_up():
            y_cor = self.paddle.ycor()
            self.paddle.sety(y_cor + 50)

        def move_down():
            y_cor = self.paddle.ycor()
            self.paddle.sety(y_cor - 50) 

        screen.listen()
        screen.onkey(fun=move_up, key=up_key)
        screen.onkey(fun=move_down, key=down_key)

    def paddle_as_computer(self, ball_ycor):
        
        self.paddle.sety(ball_ycor)

        
        
        