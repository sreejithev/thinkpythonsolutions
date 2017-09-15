s = 'spam'
t = list(s)
print t

s = 'pining for the fjords'
p = s.split()
print p

a = 'spam-spam-spam'
delimeter = '-'
k = a.split(delimeter)
print a

b = ['pining', 'for', 'the', 'fjords']
delimeter = ' '
c = delimeter.join(b)
print c
