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
def print_hist(h):
	for c in h:
		print c, h[c]

print print_hist(h)
