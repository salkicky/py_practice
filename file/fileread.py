# GET FILENAME
name = raw_input('Enter File Name:')
print "accept:"+name

print "pattern1---------"
for line in open(name,'r'):
  print line

print "pattern2---------"
f = open(name,'r')
for line in f:
  print line
f.close()

print "pattern3---------"
f = open(name,'r')
s = f.read()
print s
f.close()

print "----------------"
for line in open(name,'r'):
  items = line.split(',')
  print "items   = "+`items`
  numbers = [int(items[0]),float(items[1]),int(items[2])]
  print "numbers = "+`numbers`