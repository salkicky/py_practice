#encoding:shift-jis

# http://d.hatena.ne.jp/nullpobug/20120401/1333206240
# 

import csv

csvfile = open('csvfile.csv')
if csvfile != None:
	for row in csv.reader(csvfile):
		for col in row:
			print col.decode("cp932")
csvfile.close

print "��������DictReader���g��"

reader = csv.DictReader(open('csvfile.csv'))
if csvfile != None:
	for record in reader:
		print record['���x��']
		print record['�p��']
		print record['���{��']
