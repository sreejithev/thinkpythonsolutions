import math
def distance(x1, y1, x2, y2):
	dx = x2 - x1
	dy = y2 - y1
	dsquare = dx ** 2 + dy **2
	result = math.sqrt(dsquare)
	#return result
	print 'dx is', dx
	print 'dy is', dy
	print 'dsquare is', dsquare
	print 'sqrt(sqrd)',result
	return 0.0
distance(1, 2, 4, 6)
