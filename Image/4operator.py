# codin: utf-8
import Image

class ImOpe:

    def __init__(self, a_fname):
        #初期化
        self.ima = Image.open(a_fname)
        self.in_pics = list(self.ima.getdata())
        self.out_pics = self.in_pics
        self.size = list(self.ima.size)

    def pos(self, a_x, a_y):
        #画素位置の獲得
        return a_y * self.size[0] + a_x

    def calRgb(self, a_p0, a_p1, func):
        #RGBモード用の計算ルーチン
        l_out_r = func(a_p0[0], a_p1[0])
        l_out_g = func(a_p0[1], a_p1[1])
        l_out_b = func(a_p0[2], a_p1[2])
        return (l_out_r, l_out_g, l_out_b)

    def diff(self, a, b):
        #差分関数
        return (a-b)

    def bibun1(self, ina):
        for y in range(self.size[1]-1):
            for x in range(self.size[0]):
                l_p0 = ina[self.pos(x,y)]
                l_p1 = ina[self.pos(x, y+1)]
                self.out_pics[self.pos(x,y)] = self.calRgb(l_p0, l_p1,
                                                           lambda m,n:self.diff(m,n))
    
    def raprasian(self, ina):
        for y in range(1, self.size[1]-1):
            for x in range(1, self.size[0]-1):
                p1 = self.pos(x, y-1)
                p3 = self.pos(x-1, y)
                p4 = self.pos(x, y)
                p5 = self.pos(x+1, y)
                p7 = self.pos(x, y+1)
                l_ret = [0,1,2]
                for i in range(3):
                    l_ret[0] = ina[p1][i] + ina[p3][i] -4*ina[p4][i]+ina[p5][i]+ina[p7][i]
                self.out_pics[p4] = (l_ret[0], l_ret[1], l_ret[2])

    def saveim(self, fname,mode):
        om = Image.new(mode, self.size, (0))
        om.putdata(self.out_pics)
        om.save(fname, "JPEG")

if __name__=='__main__':
    try:
        fname = raw_input("Input Image：")
        im = ImOpe(fname)
        print fname, im.ima.format, im.ima.mode, im.size
        
        im.bibun1(im.in_pics)
        im.raprasian(im.in_pics)

        fname = raw_input("Output Image：")
        im.saveim(fname, "RGB")
        
    except:
        print "ERROR"
