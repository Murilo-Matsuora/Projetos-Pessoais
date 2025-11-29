from turtle import Screen, Turtle
from circle import Circle
import random

SCREEN_HEIGHT = 720
SCREEN_WIDTH = 1280

def create_obj_circle(diameter, center_x, center_y):
    return Circle(diameter, center_x, center_y)

def generate_ray(trgt_x, trgt_y):
    ray.clear()
    ray.pu()
    ray.goto(0, 0)
    ray.pd()
    ray.dot(8,"lightgreen")
    ray.setheading(ray.towards(trgt_x, trgt_y))
    while -SCREEN_WIDTH/2 < ray.xcor() < SCREEN_WIDTH/2 and -SCREEN_HEIGHT/2 < ray.ycor() < SCREEN_HEIGHT/2:
        for obj in objs:
            dist = ray.distance(obj.center_x, obj.center_y)
            if dist <= obj.diameter/2:
                incidence_angle = ray.heading()
                normal = ray.towards(obj.center_x, obj.center_y)
                delta = (incidence_angle - normal)
                reflected_angle = (incidence_angle - 2 * delta) + 180
                ray.setheading(reflected_angle)
                while ray.distance(obj.center_x, obj.center_y) <= obj.diameter/2:
                    ray.forward(1)
                break
        ray.forward(1)
        
    
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onclick(fun=generate_ray)

objs = []
for i in range(50):
    diameter = random.randint(20, 100)
    center_x = random.randint(-SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    center_y = random.randint(-SCREEN_HEIGHT/2, SCREEN_HEIGHT/2)
    c = create_obj_circle(diameter, center_x, center_y)
    objs.append(c)

screen.update()

# screen.tracer(1)
ray = Turtle(visible=False)
ray.dot(8,"lightgreen")
ray.speed(0)
ray.color("lightgreen")

ray.pensize(2)

while True:
    # generate_ray(0, 0, -0.99, -1)
    screen.update()


screen.exitonclick()
