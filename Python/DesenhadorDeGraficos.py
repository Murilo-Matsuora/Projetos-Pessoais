from turtle import Turtle, Screen

SETUP_WIDTH = 1200
SETUP_HEIGHT = 800
NUMBERS_SPACING = 20
PRECISION = 0.5

def draw_x_axis():
    graph.pu()
    graph.goto(- SETUP_WIDTH/2, 0)
    graph.pd()   
    graph.seth(0)
    graph.forward(SETUP_WIDTH) 
    
def draw_y_axis():
    graph.pu()
    graph.goto(0, - SETUP_HEIGHT/2)
    graph.pd()
    graph.seth(90)
    graph.forward(SETUP_HEIGHT)
    
def draw_numbers_in_x_axis():
    graph.pu()
    graph.goto(- SETUP_WIDTH/2, 0)
    graph.pd()  
    for i in range(round(SETUP_WIDTH / NUMBERS_SPACING)):
        graph.seth(0)
        graph.forward(NUMBERS_SPACING)
        graph.seth(90)
        graph.forward(5)
        graph.seth(270)
        graph.forward(10)

        graph.pu()
        graph.forward(10)
        graph.write(arg=f"{i - round((SETUP_WIDTH / NUMBERS_SPACING) / 2) + 1}", align="center", font=('Arial', 6, 'normal'))
        graph.seth(90)
        graph.forward(10)
        graph.pd()
        
        graph.forward(5)

def draw_numbers_in_y_axis():
    graph.pu()
    graph.goto(0, - SETUP_HEIGHT/2)
    graph.pd()
    for i in range(round(SETUP_HEIGHT / NUMBERS_SPACING)):
        graph.seth(90)
        graph.forward(NUMBERS_SPACING)
        graph.seth(0)
        graph.forward(5)
        graph.seth(180)
        graph.forward(10)

        graph.pu()
        graph.forward(10)
        if i - round(SETUP_HEIGHT / NUMBERS_SPACING) / 2 + 1 != 0:
            graph.write(arg=f"{i - round((SETUP_HEIGHT / NUMBERS_SPACING) / 2) + 1}", align="center", font=('Arial', 6, 'normal'))
        graph.seth(0)
        graph.forward(10)
        graph.pd()

        graph.forward(5)

def function(x):
    return 1/50 * x * x

def draw_function():
    # graph.pu()
    # graph.goto(- SETUP_WIDTH/2, 0)
    # graph.pd()
    graph.speed(0)
    
    x = - (SETUP_WIDTH / 2) / NUMBERS_SPACING
    while x < (SETUP_WIDTH / 2) / NUMBERS_SPACING:
        graph.pu()
        graph.goto(x * NUMBERS_SPACING, function(x) * NUMBERS_SPACING)
        # print(f"x = {x}, f(x) = {function(x)}, pos = {graph.pos()}")
        graph.pd()
        graph.dot(4, "red")
        x += PRECISION

screen = Screen()
screen.setup(SETUP_WIDTH, SETUP_HEIGHT)

graph = Turtle()
graph.speed(0)
graph.hideturtle()

print(f"Final graph will be {SETUP_WIDTH / NUMBERS_SPACING} x {SETUP_HEIGHT / NUMBERS_SPACING}")

draw_x_axis()
draw_y_axis()
draw_numbers_in_x_axis()
draw_numbers_in_y_axis()

draw_function()




screen.exitonclick()
