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
person = input("what's your name")
print ("hello", person)

while(True):
    number = int(input("how many sides"))
    print(number)
    if number == 0:
        break #break here

    for i in range(number):
        pendown()
        right(360/number)
        forward(100)
        penup()

# Close window on click.
exitonclick()
