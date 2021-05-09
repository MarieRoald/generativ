from turtle import *
from PIL import Image
from turtle_tools import draw_background


tracer(0, 0)
speed(0)
def tegn_firkant(lengde):
  for kant in range(4):
    forward(lengde)
    right(90)
    
skjerm = Screen()
skjerm.setup(800, 800)
skjerm.bgcolor('#112620')
draw_background()

speed(0)

farger = ['#A6372D', '#F29A2E', '#FFFFFF']
for i, farge in enumerate(farger):
  color(farge)
  pensize(5-2*i)
  home()
  for lengde in range(10, 250, 1):
    tegn_firkant(lengde)
    right(5)
  
update()

hideturtle()
cv = getcanvas()
cv.postscript(file="firkantspiral.ps", colormode='color')
img = Image.open('firkantspiral.ps')
img.save('firkantspiral.png', 'png')


done()
