#import math
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def polygon(t, n, length):
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def circle(t, r):
	""" Draws a circle with the given radius.
	t : Turtle
	r : radius
	"""

	circumference = 2 * math.pi * r
	n = int(circumference /3) +1
	length = circumference / n
	polygon(t, n, length)

polygon(bob,50, 2)
