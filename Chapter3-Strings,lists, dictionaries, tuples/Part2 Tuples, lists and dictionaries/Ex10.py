tmp=input().split(' ')
m,n=int(tmp[0]),int(tmp[1])
a=1
for i in range(m):
    for j in range(n):
        print(a,end=' ')
        a+=1
    print('')