# coding: utf-8

normal = [2,8,4,10,1,6,7]         #通常の配列宣言
print normal                     #配列表示 [2,8,4,10,1,6,7]
normal.sort()                    #小さい順にｿｰﾄ
print normal                     #配列表示 [1,2,4,6,7,8,10]

array = map(list, [()]*10)     #要素10の空配列を作成 
print array                        #配列表示 [[],[],[],[],…[]]
for i in range(10):              #配列に0～9を入力（ここで0～10を入れようとすると配列数違いでｴﾗｰ）
    array[i] = 9-i
print array                        #配列表示 [9,8,7,6,5,4,3,2,1,0]

tmp = array
tmp.sort()
print tmp

def inverse(x,y):                 #sort時の値評価に使う関数。2ﾒﾝﾊﾞの比較なので、必ず入力は2つにする。
    return y-x
tmp.sort(inverse)               # inverseで評価を行いｿｰﾄ
print tmp
