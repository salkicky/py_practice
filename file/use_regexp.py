#encoding:shift-jis

import re


f = open("file.txt",'r')
s = f.read()
f.close()

print s

r = re.compile("([1-9])")

for line in open("file.txt",'r'):
	m = r.search(line)
	print m
	print m.groups()

m = r.search("4 5 a 9")
print m
print m.groups()
