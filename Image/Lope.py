# coding: utf-8
import Image

class ImOpe:
    def __init__(self, fname):
        self.im = Image.open(fname)
        self.in_pics = list(self.im.getdata())
        self.out_pics = self.in_pics
        self.size = list(self.im.size)

    def pos(self, a_o, a_x, a_y):
        return a_o + (a_y * self.size[0] + a_x)

    def raprasian(self, pics):
        for y in range(3, self.size[1]-3):
            for x in range(3, self.size[0]-3):
                po = self.pos(0,x,y)
                p1 = pics[self.pos(po,0,-1)]
                p3 = pics[po-10]   #なぜ正しく出ない？
                p4 = pics[po]
                p5 = pics[self.pos(po,1,0)]
                p7 = pics[self.pos(po,0,1)]
                print x,y,"=",p1,p3,p4,p5,p7,"PO",po
                self.out_pics[po] = p1+p3-4*p4+p5+p7

    def save(self, fname,mode):
        om = Image.new(mode, self.size, (0))
        om.putdata(self.out_pics)
        om.save(fname, "JPEG")

if __name__=='__main__':
    try:
        fname = raw_input("Input Image：")
        fi = ImOpe(fname)
        print fname, fi.im.format, fi.im.mode, fi.size

        fi.raprasian(fi.in_pics)
#        for y in range(0, fi.size[1]):
#            for x in range(0, fi.size[0]):
#                print x,y, fi.in_pics[fi.pos(x,y)]

        fname = raw_input("Output Image：")
        fi.save(fname, "L")
    except:
        print "ERROR"
