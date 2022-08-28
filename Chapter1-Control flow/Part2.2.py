n=int(input())
i=1
while (i<=n):
  print(' '*(n-i)+'*'*(2*i-1)+' '*(n-i))
  i+=1
while (i<=2*n-1):
  print(' '*(i-n)+'*'*(4*n-2*i-1)+' '*(i-n))
  i+=1 