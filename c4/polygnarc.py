import math
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def polygon(t, n, length):
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, length)
def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length /3) + 1
	step_length = arc_length / n
	step_angle = float(angle) / n

	for i in range(n):
		fd(t, step_length)
		lt(t, step_length)
	polygon(t, n, length)

arc(bob, 50, 50)
wait_for_user()
