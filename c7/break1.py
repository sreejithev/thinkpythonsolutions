x = input()
y = input()
a = input()
while True:
	print x
	y = (x + a / x) / 2
	if y == x:
		break
	x = y
