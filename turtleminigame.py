from turtle import *

#DEFINITION
#Create a turtle that can move in 4 directions
#Have an end goal
#Have visual feedback when goal is reached

#region Initial Information
move_distance = 50
speed(0)
bgcolor("#D2691E")
#endregion

#region Ocean
color("blue")
penup()
goto(300, 550)
pendown()
begin_fill()
goto(300, -550)
goto(700, -550)
goto(700, 550)
goto(300, 550)
end_fill()
#endregion



#region Turtle
penup()
goto(-400, 0)
color("green")
shapesize(1.5, 1.5, 1.5)
shape("turtle")
#endregion

#region Movement
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

onkey(move_up, "Up")
onkey(move_down, "Down")
onkey(move_left, "Left")
onkey(move_right, "Right")
listen()
#endregion

#region Goal
def check_goal():
    if xcor() > 300:
        hideturtle()
        goto(0, 0)
        color("White")
        write("YOU WIN!")

        onkey(None, "Up")
        onkey(None, "Down")
        onkey(None, "Left")
        onkey(None, "Right")
#endregion

done()

