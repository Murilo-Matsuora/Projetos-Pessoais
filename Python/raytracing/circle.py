from turtle import Turtle
TURTLE_diameter = 20

class Circle(Turtle):
    def __init__(self, diameter, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        self.diameter = diameter
        self.pu()
        self.shape("circle")
        self.color("white")
        self.shapesize(diameter/20)
        self.goto(center_x, center_y)
