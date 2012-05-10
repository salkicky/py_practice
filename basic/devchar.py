s = "python."
target1 = "t"
target2 = "o"

for i in range(7):
  if s[i]==target1:
    k1 = i
  elif s[i]==target2:
    k2 = i
  else:
    pass

print s[0:k1]
print s[k1:k2]
print s[k2:7]
print "------------"

s = "3, 4.5, 7,"
mark = ","
item = ["s","s","s"]

index = 0
k = 0
for i in range(10):
  if s[i]==mark:
    item[index] = s[k:i]
    k = i+1
    index += 1
  else:
    pass

print "char0 = "+item[0]
print "char1 = "+item[1]
print "char2 = "+item[2]

num0=int(item[0])
num1=float(item[1])
num2=int(item[2])

print "num0 = "+`num0`
print "num1 = "+`num1`
print "num2 = "+`num2`
