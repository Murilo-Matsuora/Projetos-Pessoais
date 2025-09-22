from turtle import Turtle, Screen
from ball import Ball
import time
SC_WIDTH = 800
SC_HEIGHT = 600

screen = Screen()
screen.bgcolor("black")
screen.setup(SC_WIDTH, SC_HEIGHT)
screen.tracer(0)
screen.listen()

ball = Ball((0.5, 0))
screen.update()
screen.onclick(ball.launch_to)

game_over = False
while not game_over:
    time.sleep(0.01)
    screen.update()
    ball.move()

screen.exitonclick()