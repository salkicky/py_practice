fname = 'file.txt'

print "--File--read--------------"
fr = open(fname,'r')
s = fr.read()
print s
fr.close()

print "-write--------------------"
fw = open(fname,'w')
fw.write("3, 5.4, 7\n4, 2.3, 1\n")
fw.write("1, 7.6, 4\n")
fw.close()

print "--File-read---------------"
fr = open(fname,'r')
s = fr.read()
print s
fr.close()

print "--File--readline----------"
fr = open(fname,'r')
s0 = fr.readline()
s1 = fr.readline()
s2 = fr.readline()
print "s0 = "; print s0
print "s1 = "; print s1
print "s2 = "; print s2
fr.close()

print "---------------------------"
print "s0[0]   = " + s0[0]
print "s1[0:6] = " + s1[0:6]

a = int(s0[0])
b = int(s2[0])
print "s0[0] + s2[0] + 5 = "+`a+b+5`

# from decimal import *
# d = decimal(s2[3:6])
c = float(s2[3:6])
print "s2[3:6] = "+`c`

print "-write--------------------"
fw = open(fname,'w')
fw.write(" 1st line.\n 2nd line.\n")
fw.write(" 3rd line.\n 4th line.\n")
fw.close()