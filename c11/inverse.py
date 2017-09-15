print 'Enter the string'
s = raw_input()
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram(s)
print h

def invert_dict(h):
	inverse = dict()
	for key in h:
		val = h[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse
print invert_dict(h)
