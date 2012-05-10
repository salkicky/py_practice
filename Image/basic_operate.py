# coding: utf-8
import Image

try:
    name = raw_input("Input File name ：")
    filename = "./"+name
    im = Image.open(filename)
    print im.format, im.size, im.mode       #画像情報の出力
    
    #im.rotate(45).show()                       #45度回転表示
    #im.transform(picsize,"EXTENT",???) #座標変換

    #画素値を全て出力する。
    pics = list(im.getdata())       #getdata()の引数band = 0,1,2 ( R,G,B )
    #print pics

    #ﾘｽﾄのｻｲｽﾞを計算1
    size = 0
    for i in pics:
        size += 1
    print size
    #ﾘｽﾄのｻｲｽﾞを計算2
    picsize = list(im.size)
    print picsize, picsize[0]*picsize[1]

    #pics[]の最後尾のRGB値
    print pics[size-1]               #表示 (123, 56, 70)

    #輝度変換
    val = map(list, [()]*size)       #空のﾘｽﾄ生成
    for i in range(size):
        val[i] = int(0.2*pics[i][0] + 0.2*pics[i][1] + 0.6*pics[i][2])   #変換後に整数値へ直す
    print val[size-1]

    #画像のｺﾋﾟｰと保存
    #imout = im.copy()
    #imout.save("./a.jpg","JPEG")

    #ｸﾞﾚｰｽｹｰﾙ画像の生成
    #   "RGB" = 8bit×3　ﾌﾙｶﾗｰ
    #   "L"      = 8bit×1　ｸﾞﾚｲｽｹｰﾙ
    #   "1"      = 1bit×1  ２値画像
    imgray = Image.new("L",picsize,(0))             #ｸﾞﾚｲｽｹｰﾙの画像生成
    imgray.putdata(val)                                     #輝度変換した値を入力
    imgray.save("./gray.jpg","JPEG")

    #2値画像の生成
    imbw = Image.new("1",picsize,(0))
    level = int(raw_input("input_level(black&white) 0-255:"))   #閾値の入力
    for i in range(size):
        if val[i] > level:
            val[i] = 0
        else:
            val[i] = 255
    imbw.putdata(val)
    imbw.save("./bw.jpg","JPEG")
except:
    print "★ERROR★"
