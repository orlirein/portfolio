from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
# t.setposition(x_pos, y_pos)

### Write your code below:
pendown()

for x in range(4):
    right(90)
    forward(100)

penup()

setposition (50,50)
pendown ()
for x in range(3):
    right(120)
    forward(100)

penup()
# Close window on click.
exitonclick()
