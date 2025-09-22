from turtle import Turtle
import random
import math
SC_WIDTH = 800
SC_HEIGHT = 600
GRAVITY = -0.8
MAX_SPEED = 50
MINIMUM_SPEED_TO_KEEP_MOVING = 0.2

class Ball(Turtle):
    def __init__(self, initial_speed):
        super().__init__("circle", visible=True)
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.pu()

        random_x = random.randint(math.floor(-SC_WIDTH/2 + 20),math.floor(SC_WIDTH/2 - 20))
        random_y = random.randint(math.floor(-SC_HEIGHT/2 + 20), math.floor(SC_HEIGHT/2 - 20))
        # self.goto(random_x, random_y)
        self.goto(0, 0)

        self.speed_x, self.speed_y = initial_speed


    def launch_to(self, trgt_x, trgt_y):
        # delta_x = trgt_x - self.xcor()
        # delta_y = trgt_y - self.ycor()
        # speed_length = math.sqrt(delta_x**2 + delta_x**2)
        self.speed_x += (trgt_x - self.xcor()) * 0.1
        self.speed_y += (trgt_y - self.ycor()) * 0.1
        # print(f"a: {(trgt_x - self.xcor()) * 0.01}\nb: {(trgt_y - self.ycor()) * 0.01}\n")

    def apply_gravity(self):
        self.speed_y += GRAVITY

    def bounce_off_walls(self):
        if abs(self.xcor()) + 19 > SC_WIDTH / 2:
            self.goto(math.copysign(SC_WIDTH / 2 - 20, self.xcor()), self.ycor())
            self.speed_x *= -1
            self.speed_x *= 0.85
            self.speed_y *= 0.85
        elif abs(self.ycor()) + 20 > SC_HEIGHT / 2:
            self.goto(self.xcor(), math.copysign(SC_HEIGHT / 2 - 20, self.ycor()))
            self.speed_y *= -1
            self.speed_x *= 0.85
            self.speed_y *= 0.85
            if self.speed_y <= 1.5:
                self.speed_y = 0
                print(f"Speed: {self.speed_y}\nPos: {self.ycor()}")
                return
            if self.speed_y <= 9:
                self.speed_y *= 0.90
            if self.speed_y <= 5:
                self.speed_y *= 0.85
            if self.speed_y <= 4.5:
                self.speed_y *= 0.85
            if self.speed_y <= 1.5:
                self.speed_y *= 0.2
            

    def apply_friction(self):
        speed_length = math.sqrt(self.speed_x**2 + self.speed_y**2)
        # print(f"Speed: {speed_length}")
        if speed_length >= MAX_SPEED:
            max_speed_acceleration = MAX_SPEED / speed_length
            # print(f"accel {max_speed_acceleration}")
            self.speed_x *= max_speed_acceleration
            self.speed_y *= max_speed_acceleration
    
    def move(self):
        self.apply_gravity()
        self.apply_friction()
        self.bounce_off_walls()
        # print(f"spX {self.speed_x}\nspY {self.speed_y}\n")
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)
