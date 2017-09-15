s = 'abc'
t = [0, 1, 2]
z = zip(s, t)
print z

p = zip('anne', 'elk')
print p

q = [('a', 0), ('b', '1'), ('c', '2')]
for letter, number in q:
	print number, letter
