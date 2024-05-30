from turtle import *
from random import *

#DEFINITION
#Create a star system on a black background
#Random star size and position
#Use for loop to generate a large amount of stars


# Fullscreen the canvas


bgcolor("black")
hideturtle()

width = window_width()
height = window_height()

def draw_star(xpos: int, ypos: int) -> None:

  penup()
  goto(xpos, ypos)
  pendown()
  size = randrange(5, 20)
  dot(size, "white")

for i in range(100):
  draw_star(randrange(round(-width / 2), round(width / 2)), randrange(round(-height / 2), round(height / 2)))

done()