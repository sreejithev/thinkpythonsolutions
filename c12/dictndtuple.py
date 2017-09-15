d = {'a' : 0, 'b' : 1, 'c' : 2}
t = d.items()
print t

s = [('a', 0), ('c' , 2), ('b' , 1)]
a = dict(s)
print a

k = dict(zip('abc', range(3)))
print k

for key, val in k.items():
	print val, key
