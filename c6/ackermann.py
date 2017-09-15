def ackermann(m, n):
	""" compute the ackermann function A(m, n)
	m, n : non negative integers
	"""
	if m == 0:
		return n + 1
	if n == 0:
		return ackermann(m - 1, 1)
	return ackermann(m - 1, ackermann(m, n - 1))
print ackermann(3, 4)
