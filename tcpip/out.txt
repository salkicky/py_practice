import tcpip

#fname = '../file/file.txt'
fname = raw_input('Input File Name =:')

f = open(fname,'r')
l_data = f.read()
f.close()

tcpip.send_end(l_data)