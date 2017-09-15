import math
def estimate_pi():
	""" computes an estimate of pi.
	algorithm due to srinivasa ramanujan
	"""

	total = 0
	k = 0
	factor = 2 * math.sqrt(2) / 9801
	while True:
		num = factorial(4 * k) * (1103 + 26390 * k)
		den = factorial(k) ** 4 * 396 ** (4 * k)
		total += term

		if abs(term) < 1e - 15:
			break
	return 1 / total
print estimate_pi() 
