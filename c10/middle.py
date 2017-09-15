s = [1,2,3,4,5]
def middle(s):
	del s[0],s[-1]
	return s
print middle(s)
