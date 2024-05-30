from turtle import *
from random import *

#DEFINITION
#Creating a Balloon Popper using Python Turtle
#Be able to detect inputs
#Require multiple inputs to pop the balloon
#Utilize variables, conditions and functions


# Fullscreen the canvas
screen = Screen()
screen.setup(1.0, 1.0)

# Set up balloon and randomize its pop limit
diameter = 40
pop_diameter = randint(100,250)
colors = ["red", "green", "blue", "brown", "pink", "purple", "orange"]

# balloon
def draw_balloon():
  dot(diameter)

draw_balloon()

# inflate said balloon
def inflate_balloon():
  global diameter
  global colors
  diameter = diameter + randint(10, 20)
  draw_balloon()
  if diameter >= pop_diameter:
    clear()
    diameter = 40
    color(choice(colors))
    write("POP!")

draw_balloon()

# run inflate_balloon function when up arrow is pressed
onkey(inflate_balloon, "Up")
listen()



done()
  