from turtle import Turtle, Screen
from paddle import Paddle
from scoreofpong import Scoreboard
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)



ball = Ball()
score = Scoreboard()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))




screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # update the screen and show everything 
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # bounce the ball
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses the ball
    if ball.xcor()> 380: # cause paddle have width of 350
        ball.reset_position()
        score.l_point()
        

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

        
    


screen.exitonclick()
