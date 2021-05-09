from p5 import *


def setup():
    width = 1000
    height = 1000
    size(width, height)
    rect_mode("CENTER")
    pass


def draw():
    color_mode('HSB', 360, 100, 100)
    background( 22, 23, 95)

    translate(width/2, height/2)

    no_stroke()
    fill(163, 44, 55)
    rect(0, 0, 300, 400)
    fill(163, 44, 50)
    rect(0, -200-50, 200, 100)

    fill(22, 61, 85)
    for i in range(5):
        rect( 80, 200 + 5 + 10*i, 50, 9)
        rect(-80, 200 + 5 + 10*i, 50, 9)
    fill(22, 61, 100)
    rect( 80, 200 + 5 + 50, 80, 9)
    rect(-80, 200 + 5 + 50, 80, 9)

    fill(22, 61, 100)
    stroke(22, 61, 85)
    stroke_weight(2)
    rect(-100, -150, 20, 30)
    rect(-100, -115, 20, 20)

    no_stroke()
    fill(22, 61, 85)
    for i in range(10):
        rect(-155 - 10*i, -120, 9, 80*(1.02**i))
        rect(155 + 10*i, -120, 9, 80*(1.02**i))

    fill(186, 40, 25)
    rect(-55, -250, 50, 50 )
    rect( 55, -250, 50, 50 )
    
    no_loop()
    save("enrobot.png")


run()
