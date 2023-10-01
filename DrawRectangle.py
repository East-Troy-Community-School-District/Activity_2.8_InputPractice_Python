'''
DrawRectangle
Pawelski
10/1/2023
Introduction to Computer Science
'''

import turtle
import time

t = turtle.Turtle()

length = turtle.numinput("Length",
                         "Enter the length of the rectangle you want to draw:")
width = turtle.numinput("Width",
                        "Enter the width of the rectangle you want to draw:")

t.forward(length)
t.left(90)
t.forward(width)
t.left(90)
t.forward(length)
t.left(90)
t.forward(width)
t.left(90)

time.sleep(5)
t.reset()

# Add your code here!


turtle.mainloop()