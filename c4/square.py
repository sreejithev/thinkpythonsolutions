from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
t = Turtle()
print bob
print t

def square(t):
	for i in range(4):
		fd(t, 100)
		lt(t)
square(t)
square(bob)

wait_for_user()
