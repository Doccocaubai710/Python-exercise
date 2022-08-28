n=int(input())
s=input()
dic=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result=[dic[(dic.index(i)+n)%26] if i in dic else ' ' for i in s]
for re in result:
    print(re,end='')