#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 1
# This program computes the volume and surface area of a sphere from a user inputed radius
#------------------------------------------------------------------------------

from math import pi as p

frac = 4/ 3.0
r = float(input("Enter the radius of the sphere: "))
SA = 4*p*r**2
vol = frac*p*r**3

print("The volume is: "+str(vol))
print("The surface area is: "+str(SA))