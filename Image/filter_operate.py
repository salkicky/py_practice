# coding: utf-8
import Image

class ImOpe:
    size = map(list, [()]*2)                  #画像ｻｲｽﾞ
    mode = ""
    format = ""
    in_pics = {}
    out_pics = {}
    
    def __init__(self, in_name):
        ima = Image.open(in_name)
        self.size = list(ima.size)
        self.in_pics = list(ima.getdata())
        self.mode = ima.mode
        self.format = ima.format
        self.out_pics = self.in_pics

    def getpos(self, a_x, a_y):
        #横方向のﾗｽﾀｰ走査で得た画素列の中で、目的の座標値の画素位置を得る。
        return a_y*self.size[0] + a_x
    
    def diff(self, a_p0, a_p1):
        #RGBで渡された2画素の差分を、RGBそれぞれ計算して、1画素として返す。
        l_out_r = a_p0[0] - a_p1[0]
        l_out_g = a_p0[1] - a_p1[1]
        l_out_b = a_p0[2] - a_p1[2]
        return (l_out_r, l_out_g, l_out_b)

    def operator4x4(self, a_pic, 

    def bibun1(self, ina):
        #縦方向の微分
        for y in range(self.size[1]):
            for x in range(self.size[0]-1):
                l_pics0 = ina[self.getpos(x,y)]
                l_pics1 = ina[self.getpos(x, y+1)]
                self.out_pics[self.getpos(x,y)] = self.diff(l_pics0, l_pics1)
                
    def bibun2(self, ina):
        #横方向の微分
        for x in range(self.size[0]-1):
            for y in range(self.size[1]):
                l_pics0 = ina[self.getpos(x, y)]
                l_pics1 = ina[self.getpos(x+1, y)]
                self.out_pics[self.getpos(x,y)] = self.diff(l_pics0, l_pics1)

try:
    in_name = raw_input("Input Filename：")
    out_name = raw_input("Output Filename：")

    #入力画像の読み込み
#    im = Image.open(in_name)
#    print "  " , in_name, "=", im.format, im.size, im.mode
#    data = list(im.getdata())
    c = ImOpe(in_name)
    print " " , in_name, "=", c.format, c.size, c.mode

    #ﾌｨﾙﾀ処理
#    c.bibun1(c.in_pics)
#    c.bibun1(c.out_pics)
    c.bibun2(c.in_pics)

    #結果の出力
    print "Go Output"
    om = Image.new("RGB",list(c.size),(0))
    om.putdata(c.out_pics)
    om.save(out_name,"JPEG")
    
except:
    print "ERROR"
