# META sample --------------------------------

x = 4

def apple(x=x):
  return x*2

y = apple()
print y

#--------------

from math import sin,cos

def compose1(fun1, fun2):
  def inner(x):
    return fun1(fun2(x))
  return inner

sincos = compose1(sin, cos)
x = sincos(3)
print x

def fun1(x):
  return x + " world!"

def fun2(x):
  return "Hello"

sincos = compose1(sin, cos)
x = sincos(3)
print x

def compose2(f1, f2):
  return lambda x,f1=f1,f2=f2: f1(f2(x))

sincos = compose2(sin, cos)
x = sincos(3)
print x