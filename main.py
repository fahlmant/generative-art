
# Python code to draw snowflakes fractal. 
import turtle 
import random 
  
# setup the window with a background color 
wn = turtle.Screen() 
wn.bgcolor("black") 
  
# assign a name to your turtle 
elsa = turtle.Turtle() 
elsa.speed(100) 
  
# create a list of colours 
sfcolor = ["red", "yellow", "green", "blue", "orange", "purple", "white"] 
  
def sunburst(xsize, ysize):
    elsa.color(random.choice(sfcolor)) 
    #elsa.begin_fill()
    for x in range (0,xsize):
      elsa.forward(xsize)
      elsa.left(ysize)
#        if abs(elsa.pos()) < 1:
#            break
    #elsa.end_fill()

# loop to create 20 different sized snowflakes  
# with different starting co-ordinates 
for i in range(5): 
    x = random.randint(-200, 200) 
    y = random.randint(-200, 200) 
    xsize = random.randint(100, 300) 
    ysize = random.randint(100, 300)
    elsa.penup() 
    elsa.goto(x, y) 
    elsa.pendown()
    sunburst(xsize, ysize)
  
# leave the window open until you click to close   
wn.exitonclick()   
