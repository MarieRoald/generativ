import turtle


def draw_background():
    """ Draw a background rectangle. """
    # Function by martineau on stack overflow
    # URL: https://stackoverflow.com/questions/13537483/when-saving-turtle-graphics-to-an-eps-file-the-background-color-shows-on-the-s
    a_turtle = turtle.Turtle()
    turtle.hideturtle()
    ts = a_turtle.getscreen()
    canvas = ts.getcanvas()
    height = ts.getcanvas()._canvas.winfo_height() + 10
    width = ts.getcanvas()._canvas.winfo_width()

    turtleheading = a_turtle.heading()
    turtlespeed = a_turtle.speed()
    penposn = a_turtle.position()
    penstate = a_turtle.pen()

    a_turtle.penup()
    a_turtle.speed(0)  # fastest
    a_turtle.goto(-width/2-2, -height/2+3)
    a_turtle.fillcolor(turtle.Screen().bgcolor())
    a_turtle.begin_fill()
    a_turtle.setheading(0)
    a_turtle.forward(width)
    a_turtle.setheading(90)
    a_turtle.forward(height)
    a_turtle.setheading(180)
    a_turtle.forward(width)
    a_turtle.setheading(270)
    a_turtle.forward(height)
    a_turtle.end_fill()

    a_turtle.penup()
    a_turtle.setposition(*penposn)
    a_turtle.pen(penstate)
    a_turtle.setheading(turtleheading)
    a_turtle.speed(turtlespeed)
