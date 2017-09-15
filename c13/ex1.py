import string
print string.punctuation

def make_word_dict():
	d = dict()
	fin = open ('greatpush.txt')
	for line in fin:
		word = line.strip().lower()
		d[word] = word
#	for letter in ['a', 'i', ' ']:
#		d[letter] = letter
	return d
print make_word_dict()
