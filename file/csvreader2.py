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

print "ここからDictReaderを使う"

reader = csv.DictReader(open('AutoCtrl_Area01_01.csv'))
if csvfile != None:
	for record in reader:
		print record['時間'] + "   " + record[' 設定天井照度']
		print int(record[' 白色出力値']) * int(record[' 設定天井照度'])
        record.line
