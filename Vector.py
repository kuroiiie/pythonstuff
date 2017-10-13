#------------------------------------------------------------------------------
# Chloe Jiang
# cfjiang@ucsc.edu
# programming assignment 7
"""
This module provides functions to perform standard vector operations.  Vectors
are represented as lists of numbers (floats or ints).  Functions that take two 
vector arguments may give arbitrary output if the vectors are not compatible,
i.e. of the same dimension.  
"""
#------------------------------------------------------------------------------
# import standard library modules
#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------

import math
import random

rand = random.Random()

def tester(u, v):
	if (len(u) == len(v)):
		return True
	return False

def add(u, v):
	if (tester(u, v) == True):
		x = [0]*len(v)
		for i in range(len(v)):
			x[i] = u[i] + v[i]
		return x

def negate(u):
	x = u[:]
	for i in range(len(u)):
		x[i] *= -1
	return x;

def sub(u, v):
	if (tester(u, v) == True):
		return add(u, negate(v))

def scalarMult(c, u):
	x = u[:]
	for i in range(len(u)):
		x[i] *= c
	return x

def zip(u, v):
	if (tester(u, v) == True):
		x = [0]*len(v)
		for i in range(len(v)):
			x[i] = u[i]*v[i]
		return x

def dot(u, v):
	if (tester(u, v) == True):
		dot = 0
		x = zip(u, v)
		for i in range(len(x)):
			dot += x[i]
		return dot

def length(u):
	return math.sqrt(dot(u, u))

def unit(v):
	x = v[:]
	for i in range(len(v)):
		x[i] /= length(v)
	return x

def angle(u, v):
	if (tester(u, v) == True):
		return math.degrees(math.acos(dot(unit(u),unit(v))))

def randVector(n, a, b):
	v = [0]*n
	for i in range(len(v)):
		v[i] = rand.uniform(a, b)
	return v
