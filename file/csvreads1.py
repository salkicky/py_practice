#encoding:shift-jis
# CSV�t�@�C���̓ǂݍ���

import csv

filename = "file.txt"
csvfile = open(filename)
print csvfile

for row in csv.reader(csvfile):
	print row
	for elem in row:
		print elem,
	print

csvfile.close()
print csvfile

