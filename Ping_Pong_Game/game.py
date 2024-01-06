from turtle import Turtle , Screen
from paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time


game_is_on = True

# screen  setup
screen = Screen()
screen.setup(width=800 ,height= 600 )
screen.bgcolor("black")
screen.title(titlestring="PING PONG GAME")
screen.tracer(0)


#paddle setup
l_paddle = Paddle((350,0))
r_paddle = Paddle((-350,0))

#Ball Setup
ball = Ball()

#score board setup
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"w")
screen.onkey(r_paddle.go_down,"s")
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.Ball_move()

    #detecting the collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()

    #detect L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        score.r_point()


screen.exitonclick()

