from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def polygon(t, n, length,):
	""" Draws n line segments.

	t : Turtle object
	n : number of line segments
	length : length of each segment
	angle : degrees between segments
	"""

	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

polygon(bob, 7, 70)
