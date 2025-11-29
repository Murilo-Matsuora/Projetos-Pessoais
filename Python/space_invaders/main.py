import time
from turtle import Turtle, Screen

from crab import Crab

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_SPEED = 10
PERIOD = 0.01

def move_player_left():
    player.goto(player.xcor() - PLAYER_SPEED, player.ycor())

def move_player_right():
    player.goto(player.xcor() + PLAYER_SPEED, player.ycor())
    
def player_shoot():
    shot = Turtle(visible=False)
    shot.pu()
    shot.seth(90)
    shot.color("white")
    shot.goto(player.xcor(), player.ycor())
    shot.pensize(5)
    shot.pd()
    
    shots.append(shot)
    
def detect_shot_collision(curr_shot):
    for enemy in enemies:
        if curr_shot.distance(enemy.xcor(), enemy.ycor()) < enemy.size:
            enemies.remove(enemy)
            enemy.explode()
            dead_enemies.append(enemy)
    
    
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkeypress(key='a', fun=move_player_left)
screen.onkeypress(key='d', fun=move_player_right)
screen.onkeypress(key='space', fun=player_shoot)

player = Turtle()
player.pu()
player.seth(90)
player.color("white")
player.shapesize(1.5, 1.5)
player.goto(0, -SCREEN_HEIGHT/2 + 50)

shots = []

enemies = []

dead_enemies = []

for i in range(10):
    enemy = Crab()
    enemies.append(enemy)

game_is_on = True
while game_is_on:
    time.sleep(PERIOD)
    screen.update()

    for enemy in enemies:
        enemy.move()

    for dead_enemy in dead_enemies:
        if dead_enemy.decrement_timer(PERIOD):
            dead_enemies.remove(dead_enemy)
    
    for shot in shots:
        if shot.ycor() < SCREEN_HEIGHT/2 + 15:
            shot.clear()
            shot.forward(10)
            
            detect_shot_collision(shot)
            
        else:
            shots.remove(shot)
