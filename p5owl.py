from p5 import *
import random
from random import randint


def setup():
    size(2*1920, 2*1080)
    stroke_weight(2)

def equilateral_triangle(center_x, center_y, width):
    triangle((center_x, center_y),
             (center_x - width/2, center_y - 0.5*sqrt(3)*width),
             (center_x + width/2, center_y - 0.5*sqrt(3)*width))

def random_color():
    return randint(200, 255), randint(200, 255), randint(200, 255)

def eyes(center_x, center_y, radius, distance, eyelid_width, eyelid_height, eyelid_open=True,):
    if eyelid_open:
        angle = (PI, TWO_PI)
    else:
        angle = (0, PI)

    eyelid_position = center_y + 0.25*eyelid_height

    offset = radius/2 + distance / 2
    circle(center_x + offset, center_y, radius, mode="CENTER")
    arc((center_x + offset, eyelid_position), eyelid_width, eyelid_height, *angle)
    circle(center_x - offset, center_y, radius, mode="CENTER")
    arc((center_x - offset, eyelid_position), eyelid_width, eyelid_height, *angle)

def body(center_x, top_y, width, height, feather_height, color):
    fill(*color)
    arc((center_x, top_y), width, height, 0, PI) # 180 degrees
    fill(255)
    arc((center_x, top_y), width, feather_height, 0, PI) # 180 degrees

def owl(center_x, center_y, owl_width, owl_height, feather_height,
        nose_offset, nose_width, eye_offset, eye_radius, eye_distance,
        eyelid_width, eyelid_height, eyelid_open, color
    ):
    top_y = center_y - owl_height / 4
    nose_offset += feather_height / 2
    body(center_x, top_y, owl_width, owl_height, feather_height, color)

    equilateral_triangle(center_x, top_y + nose_offset, nose_width)
    eyes(
        center_x=center_x,
        center_y=top_y + nose_offset - eye_offset - nose_width*0.5*sqrt(3),
        radius=eye_radius,
        distance=eye_distance,
        eyelid_width=eyelid_width,
        eyelid_height=eyelid_height,
        eyelid_open=eyelid_open
    )
ran = False
def draw():
    global ran
    background(255, 255, 255)

    no_fill()
    stroke(0)

    num_x = 20
    num_y = 8
    
    center_y = height / num_y / 2
    for i in range(num_y):
        center_x = width / num_x / 2
        if i % 2 == 0:
            num_x_curr = num_x
        else:
            num_x_curr = num_x - 1
            center_x += width / num_x / 2

        for j in range(num_x_curr):
            owl_width = randint(width // num_x // 3 - 10, width // num_x - 10)
            owl_height = randint(height // num_y // 1.5, 1.5 * height // num_y)
            feather_height = randint(owl_height // 20, owl_height // 3)
            nose_offset = randint((owl_height - feather_height) // 8, (owl_height - feather_height) // 2)
            nose_width = randint(2, 20)
            eye_offset = randint(5, 10)
            eye_radius = randint(10, 40)
            eye_distance = randint(0, 5)
            eyelid_width = randint(2, 10)
            eyelid_height = randint(2, 10)
            eyelid_open = randint(0, 1)
            color = random_color()

            owl(
                center_x=center_x,
                center_y=center_y,
                owl_width=owl_width,
                owl_height=owl_height,
                feather_height=feather_height,
                nose_offset=nose_offset,
                nose_width=nose_width,
                eye_offset=eye_offset,
                eye_radius=eye_radius,
                eye_distance=eye_distance,
                eyelid_width=eyelid_width,
                eyelid_height=eyelid_height,
                eyelid_open=eyelid_open,
                color=color
            )
            center_x += width / num_x
        center_y += height / num_y
    
    if ran:
        save("owls.png")
        no_loop()
    ran = True




run()
