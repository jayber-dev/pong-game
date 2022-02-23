import turtle
import ball
import paddle
import time
import score
import random

BALL_INIT_POSITION = (0,0)
INIT_RIGHT_PADDLE_POSITION = (350,0)
RIGHT_SCORE_POSITION = (20, 200)

INIT_LEFT_PADDLE_POSITION = (-350,0)
LEFT_SCORE_POSITION = (-80, 200)

game_is_on = True
clock_speed = 0.03
sleep_time = 0.03
# screen creation ---------------------------------------------------------------
screen = turtle.Screen()
screen.listen()
screen.colormode(1)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)



# in game -----------------------------------------------------------------------
ball = ball.Ball()



user_choice = screen.textinput("how many players", "1 or 2")

if user_choice == "2":
    left_player = paddle.Paddle(INIT_LEFT_PADDLE_POSITION)
    left_player.moves("w", "s")
    left_player_score = score.Score(LEFT_SCORE_POSITION)

    right_player = paddle.Paddle(INIT_RIGHT_PADDLE_POSITION)
    right_player.moves("Up", "Down")
    right_player_score = score.Score(RIGHT_SCORE_POSITION)

else:
    right_player = paddle.Paddle(INIT_RIGHT_PADDLE_POSITION)
    right_player_score = score.Score(RIGHT_SCORE_POSITION)
    right_player.moves("Up", "Down")
    left_player = paddle.Paddle(INIT_LEFT_PADDLE_POSITION)
    left_player_score = score.Score(LEFT_SCORE_POSITION)


while game_is_on:
    ball.ball_move()
    ball__ycor = ball.ycor()
    if user_choice == "1":
        left_player.paddle_as_computer(ball__ycor) 
    

    if ball.ycor() >= 295 or ball.ycor() <= -295:
        ball.bounce()

    if ball.distance(right_player.paddle) < 40 and ball.xcor() > 330:
        ball.bounce_from_paddle()
        clock_speed *= 0.9
        

    if ball.distance(left_player.paddle) < 40 and ball.xcor() < -330:
        ball.bounce_from_paddle()
        clock_speed *= 0.9
        
    if ball.xcor() > 420:
        left_player_score.score_count()
        ball.setposition(BALL_INIT_POSITION)
        right_player.paddle.setposition(INIT_RIGHT_PADDLE_POSITION)
    
    if ball.xcor() < - 420:
        right_player_score.score_count()
        ball.setposition(BALL_INIT_POSITION)
        left_player.paddle.setposition(INIT_LEFT_PADDLE_POSITION) 

    if right_player_score.score == 3:
        right_player_score.clear()
        left_player_score.clear()
        right_player_score.winner("right", right_player_score.score)
        ball.hideturtle()
        game_is_on = False
        
              
    if left_player_score.score == 3:
        left_player_score.clear()
        right_player_score.clear()
        right_player_score.winner("left", left_player_score.score)
        ball.hideturtle()
        game_is_on = False
  
        
    screen.update()
    time.sleep(clock_speed)


screen.exitonclick()






