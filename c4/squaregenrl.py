from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def square(t, length):
	""" Draws the square with sides of the given length.
	Returns the Turtle to the starting position and location.
	"""
	for i in range(4):
		fd(t, length)
		lt(t)
square(bob, 100)
