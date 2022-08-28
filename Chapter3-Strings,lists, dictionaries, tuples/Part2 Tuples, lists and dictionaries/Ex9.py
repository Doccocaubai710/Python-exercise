def transform(l):
    x=[]
    for i in l:
        if i%2==0:
            x.append(i*2)
        else:
            x.append(i*(-1))
    return x