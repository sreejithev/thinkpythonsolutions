import string
import random

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1
hist = process_file('emma.txt')

def substract(d1, d2):
	res = dict()
	for key in d1:
		if key not in d2:
			res[key] = None
	return res
words = process_file('greatpush.txt')
diff = substract(hist, words)
print ' The words in the book that are not in the word list are :'
for word in diff.keys():
	print word



