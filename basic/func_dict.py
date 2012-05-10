l_name = ["a","b","c"]
l_array = [[1,2],[]]

for i in range(2):
  print l_name[i]

func = range
for i in func(2):
  print l_name[i]

#for i in range(2):
#  print l_name[i]
#  for j in func(2):
#    print l_name[j]

# DICTIONARY TEST----------------------------
person = {'first name':"koichi",
          'last name':"hamada",
          'house':"kyoto",
          'information':""
         }
person['information'] = "futsal"
print person['first name'],person['information']

# FUNCTION TEST-----------------------------
def squre(x):
  return x*x
num = 4
print "num =",squre(num)

# TEST "or" "and"---------------------------
c = 0
d = c or squre(num)
print "d =" + `d`   #print d = 16
d = c and squre(num)
print "d =" + `d`   #print d = 0





