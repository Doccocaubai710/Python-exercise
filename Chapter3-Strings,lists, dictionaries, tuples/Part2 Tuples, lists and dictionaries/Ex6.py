size=input().split()
m,n=int(size[0]),int(size[1])
a=[]
b=[]
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))
for i in range(m):
  for j in range(n):
    print(int(a[i][j])+int(b[i][j]),end=' ')
  print('')  