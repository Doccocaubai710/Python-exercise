for i in range(100,1000,1):
  c=i%10
  b=((i-c)%10)%10
  a=i//100
  if (a**3+b**3+c**3==i):
    print(i)