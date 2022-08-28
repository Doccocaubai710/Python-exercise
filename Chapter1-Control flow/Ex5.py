from math import*


n=int(input())
Check=False
if (n<=1):
  print(Check)
if (n==2) or (n==3):
  Check=True
  print(Check)
elif (n>=4):
  Check=True
  r=int(sqrt(n))
  for i in range(2,r+1):
    if (n%i==0):
      Check=False
      break
  print(Check)