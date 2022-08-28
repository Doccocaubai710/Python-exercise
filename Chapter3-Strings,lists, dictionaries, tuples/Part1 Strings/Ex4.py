def reverse(s):
  m=''
  i=len(s)
  while i>0:
    m+=s[i-1]
    i-=1
  return m  
def mirror(s):
  dict={'b':'d','d':'b','i':'i','o':'o','p':'q','q':'p','v':'v','w':'w','x':'x',' ':' '}
  res=''
  s=reverse(s)
  for c in s:
    if c in dict:
      res+=dict[c]
    else:
      res='NOT POSSIBLE'
      break
  return res 
s=input()
print(mirror(s))