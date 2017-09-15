import math
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length)
		lt(t, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length / 3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)

arc(bob, 10, 50)


