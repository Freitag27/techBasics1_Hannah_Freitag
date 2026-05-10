#didnt have a lot of time to learn how to use turtle this week, hope its still okay 
#import turtle
from turtle import *
import random

# initial setup: canvas size
width = 400
height = 400
setup(width, height)

# set background color
bgcolor('white')

# change the color of the lines
color('#000')

# random color for circle
character_list = ['blue', 'pink', 'yellow']
c = random.choice(character_list)

# set fill color
fillcolor(c)

# draw circle
begin_fill()
circle(50, 360)  # radius & angle
end_fill()

# conditional statement
if c == 'yellow':

    # smiley
    penup()
    goto(-20, 60)
    pendown()
    dot(10, "black")
    penup()
    goto(20, 60)
    pendown()
    dot(10, "black")
    penup()
    goto(-20,40)
    pendown()
    right(90)
    circle(20, 180)
    left(90)

# quit with click
exitonclick()
