n=int(input())
i=1
while i<=n:
  space=' '*(n-i)
  for j in range(1,i):
    space+=str(j)
  space+=str(i)  
  for j in range (i-1,0,-1):
    space+=str(j)
  i+=1
  print(space)  