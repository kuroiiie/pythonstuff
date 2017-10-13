#------------------------------------------------------------------------------
#  TurtleLoop1.py
#------------------------------------------------------------------------------

import turtle
wn = turtle.Screen()      # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Pentagon")

bob = turtle.Turtle()     # Create bob the turtle to draw things
bob.pencolor("blue")
bob.pensize(10)
bob.shape('turtle')

for i in range(5):   # we don't have to do anything with the loop variable i
   bob.forward(80)   # here we just use it to 'do something' 5 times
   bob.left(72)

wn.mainloop()