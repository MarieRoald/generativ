
from p5 import *

def setup():
    width = 2000
    height = 1000
    size(width, height)
    background(33,46,64)


def draw_eyeball(x, y, r):
    with push_matrix():
        translate(x, y)

        fill(255,255,255)
        stroke_weight(0)
        circle((0, 0), r)

        color_mode('HSB', 360, 100, 100)
        fill(
            random_uniform(20, 40),
            random_uniform(40, 80),
            random_uniform(80, 95)
            )
        color_mode('RGB', 255, 255, 255)

        stroke_weight(r/20)
        stroke(33, 46, 64)
        translate(random_uniform(low=-r*0.1, high=r*0.1), 
                  random_uniform(low=-r*0.1, high=r*0.1))
        circle((0,0),
                random_uniform(0.3, 0.7)*r)

        
        translate(random_uniform(low=-r*0.05, high=r*0.05), 
                  random_uniform(low=-r*0.05, high=r*0.05))

        fill(33, 46, 64)
        stroke_weight(0)
        circle((0,0),random_uniform(0.1, 0.2)*r)

def draw():
    background(33,46,64)

    w = 120
    for i in range(0, width, w):
        for j in range(0, height, w):
            xpos = w / 2 + i + random_uniform(-10, 10)
            ypos = w / 2 + j + random_uniform(-10, 10)
            draw_eyeball(xpos, ypos, random_uniform(0.8, 1.1)*90)

    no_loop()
    save("sirkler.png")

run()
