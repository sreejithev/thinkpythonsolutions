import math
def circle_area(xc, yc, xp, yp):
	dx = xc - xp
	return dx
	dy = yc - yp
	return dy
	distance = dy - dx
	radius = distance(xc, yc, xp, yp)
	area = math.pi * distance ** 2
	result = area
	return result
print circle_area(1, 2, 4, 6)
