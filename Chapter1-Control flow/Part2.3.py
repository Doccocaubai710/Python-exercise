n=int(input())
if n==0:
  sum=0
if n==1:
  sum=1
else:
  first=0
  second=1
  for i in range(n-1):
      sum=first+second
      first=second
      second=sum
print(sum)  