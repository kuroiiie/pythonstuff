#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 2
# This program draws a star from a given number of sides
#------------------------------------------------------------------------------

import turtle
tut = turtle.Screen()
tut.title("Star")
starry = turtle.Turtle()
starry.hideturtle()
#starry.penup()
starry.speed(0)
starry.goto(-150,0)
starry.dot(10,"red")
starry.color('blue', 'lime')
starry.pensize(2)
starry.begin_fill()
n = int(input("Enter an odd integer greater than or equal to 3: "))
angle = 180-(180/n)
for i in range(n):
	#starry.pendown()
	starry.forward(300)
	starry.right(angle)
	starry.dot(10,"red")
starry.end_fill()
tut.mainloop()