x = input()
y = input()
def absolute_value(x, y):
	if x < y:
		return -1
	elif x > y:
		return 1
	elif x == y:
		return 0
print absolute_value(x, y)
