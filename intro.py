from random import*
from math import *
x = uniform(0,100)
a=float(int(input()))
while (abs(x**2-a)>=0.0000001):
  x=(x+(a/x))/2
  print('{:.7f}'.format(x),x-sqrt(a))