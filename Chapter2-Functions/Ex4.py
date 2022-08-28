def gd(a,b):
    if b==0:
        return a
    if a==0:
        return b
    if (a!=0) and (b!=0):
        if a>b:
            return gd(a%b,b)
        else:
            return gd(a,b%a)