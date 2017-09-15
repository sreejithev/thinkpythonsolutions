import math
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

def arc(t, r, angle):
        arc_length = 2 * math.pi * r * angle / 360
        n = int(arc_length / 3) + 1
        step_length = arc_length / n
        step_angle = float(angle) / n

def circle(t, r):
        circumference = 2 * math.pi * r
        n = int(circumference /3) +1
        length = circumference / n
	arc(t, r, 360)
circle(bob, 10,40)
