# coding: utf-8
import Image

try:
    in_fname = raw_input("Input Filename：")
    out_fname = raw_input("Output Filename：")

    im = Image.open(in_fname)
    indata = list(im.getdata())

    size = list(im.size)
    for i in range(size[1]):
        print i
        print indata[i]
        indata[i] = (1,4,9)
        print "a", indata[i]

except:
    print "ERROR"
