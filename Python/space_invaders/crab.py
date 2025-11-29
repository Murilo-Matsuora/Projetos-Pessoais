import time
import random
from turtle import Turtle

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

SIZE = 20
PIXEL_SIZE = 4
CRAB_PIXELART =[
    [0,0,1,0,0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,1,0,0,0],
    [0,0,1,1,1,1,1,1,1,0,0],
    [0,1,1,0,1,1,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,1],
    [0,0,0,1,1,0,1,1,0,0,0]
]

EXPLOSION_PIXELART = [
    [0,0,0,0,1,0,0,0,1,0,0,0,0],
    [0,1,0,0,0,1,0,1,0,0,0,1,0],
    [0,0,1,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,1,0,0,0,0,0,1,0,0,0],
    [1,1,0,0,0,0,0,0,0,0,0,1,1],
    [0,0,0,1,0,0,0,0,0,1,0,0,0],
    [0,0,1,0,0,1,0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0,0,1,0,0,1,0],
]

class Crab(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.pu()
        self.color("white")
        self.pensize(0)
        self.seth(270)
        self.size = SIZE
        self.draw_full_pixelart(CRAB_PIXELART)
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-10, 10)
        self.timer = 0.5
    
    def draw_pixel(self, x, y):
        self.pu()
        self.goto(x, y)
        self.pd()
        
        self.goto(x,y+PIXEL_SIZE/2)
        self.begin_fill()
        self.goto(x+PIXEL_SIZE/2,self.ycor())
        self.goto(self.xcor(),self.ycor()-PIXEL_SIZE)
        self.goto(self.xcor()-PIXEL_SIZE,self.ycor())
        self.goto(self.xcor(),self.ycor()+PIXEL_SIZE)
        self.goto(x,y+PIXEL_SIZE/2)
        self.end_fill()
    
        self.pu()
        self.goto(x, y)

    def draw_full_pixelart(self, pixelart):
        self.clear()
        inital_x = self.xcor()
        inital_y = self.ycor()
        pixelart_width = len(pixelart[0])
        pixelart_height = len(pixelart)
        for i in range(pixelart_height):
            self.goto(inital_x, inital_y-PIXEL_SIZE*i)
            self.goto(self.xcor()-((pixelart_width-1)/2 * PIXEL_SIZE), self.ycor()+(pixelart_height/2 * PIXEL_SIZE))
            for p in pixelart[i]:
                if p == 1:
                    self.draw_pixel(self.xcor(), self.ycor())
                self.seth(0)
                self.pu()
                self.forward(PIXEL_SIZE)
        self.goto(inital_x, inital_y)  
        
    
    def explode(self):
        self.draw_full_pixelart(EXPLOSION_PIXELART)

    def decrement_timer(self, period):
        self.timer -= period
        if self.timer <= 0:
            self.clear()
            return True
        return False
    
    def move(self):
        self.pu()

        if(abs(self.xcor()) > SCREEN_WIDTH/2):
            if self.xcor() > 0:
                self.goto(SCREEN_WIDTH/2, self.ycor())
            else:
                self.goto(-SCREEN_WIDTH/2, self.ycor())
            self.speed_x *= -1

        if self.ycor() > SCREEN_HEIGHT/2:
            self.goto(self.xcor(), SCREEN_HEIGHT/2)
            self.speed_y *= -1
        elif self.ycor() < -SCREEN_HEIGHT/2 + 100:
            self.goto(self.xcor(),  -SCREEN_HEIGHT/2 + 100)
            self.speed_y *= -1

        
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)
        self.draw_full_pixelart(CRAB_PIXELART)

        
