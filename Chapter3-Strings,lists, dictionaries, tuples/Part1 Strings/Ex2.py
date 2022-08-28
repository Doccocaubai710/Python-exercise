s=input()
n=len(s)
for i in range(n):
  if s[i]=='_':
    s=s.replace(s[i],' ')
s=s.title()
s=s.replace(' ','')
print(s)   