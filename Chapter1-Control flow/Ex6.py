n=int(input())
i=1
st='\\'
while i in range(n+1):
  print('_'*(n-i)+'/'+' '*(i*2-2)+st+'_'*(n-i))
  i+=1