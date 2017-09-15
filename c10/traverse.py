cheeses =['cheddar', 'edam', 'gauda']
numbers =[17, 123]
empty = []

for cheese in cheeses:
	print cheese

for i in range(len(numbers)):
	numbers[i] = numbers[i] * 2
	print numbers[i]

for x in []:
	print 'This never happens.'
