from turtle import Turtle, Screen
from PIL import Image
import numpy as np

PIXEL_SIZE = 30

def convert_image_to_matrix(image_name):
    try:
        img = Image.open(image_name)
        original_width = img.width
        original_heigth = img.height
        img = img.resize((round(img.width / PIXEL_SIZE), round(img.height / PIXEL_SIZE)))
    except FileNotFoundError:
        print("Error: Image file not found. Please check the path.")
        exit()
        
    matrix = np.array(img)
    
    # print(matrix)
    # matrix = [[(0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0)]]
    return matrix, original_width, original_heigth
    

def paint_matrix(matrix, screen):
    canv_width = screen.canvwidth
    canv_heigth = screen.canvheight
    print(f"h: {canv_heigth}")
    # n_width_pixels = round(screen.canvwidth / PIXEL_SIZE)
    # n_height_pixels = round(screen.canvheight / PIXEL_SIZE)
    
    painter = Turtle()
    
    painter.hideturtle()
    painter.speed("fastest")
    
    for row in range(len(matrix)):
        painter.pu()
        painter.goto(x= - canv_width/2 + PIXEL_SIZE, y= canv_heigth/2 - row * PIXEL_SIZE)
        painter.pd()
        for col in range(len(matrix[0])):
            # print(tuple(matrix[row][col][0 : 3]))
            painter.dot(PIXEL_SIZE, tuple(matrix[row][col][0 : 3]))
            painter.pu()
            painter.forward(PIXEL_SIZE)
            painter.pd()
            
def main():
    matrix, canvas_width, canvas_heigth = convert_image_to_matrix("pikachu.jpg")
        
    if 1080 < canvas_heigth <= 0 or 1920 < canvas_width <= 0:
        print("Invalid matrix.")
    else:
        print(f"The final painting will be {len(matrix)} x {len(matrix[0])}")
        screen = Screen()
        screen.colormode(255)
        screen.setup(height=1080, width=1920)
        screen.screensize(canvheight=canvas_heigth, canvwidth=canvas_width, bg="grey")

        paint_matrix(matrix, screen)

        screen.exitonclick()
    
main()
