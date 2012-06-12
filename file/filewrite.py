name = raw_input('Target File Name =:')

f = open(name,'w')
f.write("4, 6.7, 9\n")
f.write("2, 3.1, 0\n")
f.write("7,78.9, 4\n")
f.close()