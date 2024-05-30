from turtle import *

# Fullscreen the canvas
screen = Screen()
screen.setup(1.0, 1.0)

#PEN UP AND PEN DOWN (remove trails)
penup()
pendown()


#BACKGROUND COLOR
bgcolor("black")

#SQUARE
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
###################
#CIRCLES
color("green")
circle(50)
color("red")
circle(75)
color("purple")
circle(100)
####################
#TRIANGLE
forward(100)
left(120)
forward(100)
left(120)
forward(100)
left(120)
#####################
#FILLING SHAPES
begin_fill()
circle(50)
end_fill()

done()