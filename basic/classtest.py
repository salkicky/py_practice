
# CLASS TEST---------------------------------
class Basket:
  # rule = all function have "self".
  # rule = all class have function"__init__"" as constructor.
  def __init__(self, contents=None):
    self.contents = contents or []

  def __str__(self):
    result = ""
    for element in self.contents:
        result = result + " " + `element`
    return "Contains:"+result

  def add(self, element):
    self.contents.append(element)

  def print_me(self):
    result = ""
    for element in self.contents:
      result = result + "" + `element`
    print "Contains:"+result

ss = Basket([2,5])    #exec __init__([2,5]) and make instanse "ss".
ss.print_me()

ss.add(8)
ss.print_me()

# exec as __str__()
print ss

# SUBCLASS TEST----------------------------
class SpamBasket(Basket):
  mem1 = 1

  def func(self, a):
    self.mem1 = a

  def pr(self):
    print self.mem1

sub = SpamBasket()
sub.print_me()
sub.__init__([4,7])
sub.print_me()
ss.print_me()

sub.func(9)
print sub.mem1
sub.pr()
print sub

print "#SUBSUBCLASS TEST ----------------------------"
class Value:
  value = 0
  def __init__(self,a_val):
    self.value = a_val
  def set_value(self, a_val):
    self.value = a_val
  def print_v(self):
    print "Value =:" + `self.value`

class ItemBasket(Basket, Value):
  item = 9
  def print_all(self):
    Basket.__init__(self,[2,3])
    Value.__init__(self,200)
    print `self.item` + "#" + `self.value`
    print self

subsub = ItemBasket()
subsub.print_me()              # 'Contains:'
subsub.__init__([9,10])
subsub.print_me()              # 'Contains: 910'
subsub.print_v()                 # 'Value =:0'

subsub.set_value(12)
subsub.print_v()                 # 'Value =:12'
print subsub                     # 'Contains: 9 10'

subsub.print_all()               # '9#20'   'Contains: 2 3'

