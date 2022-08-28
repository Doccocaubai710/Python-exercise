from math import sqrt

def vector_distance(v1, v2, **kwargs):
    a=dict(**kwargs)
    m=0
    l1=0
    l2=0
    if len(a)==0:
        a={'norm':'euclidean'}
    if a['norm']=='euclidean':
        for i in range(len(v1)):
            m+=(v1[i]-v2[i])**2
        m='{:.1f}'.format(sqrt(m))
    elif a['norm']=='manhattan':
        for i in range(len(v1)):
            m+=abs(v1[i]-v2[i])
    elif a['norm']=='cosine':
        for i in range(len(v1)):
            m+=v1[i]*v2[i]
            l1+=v1[i]**2
            l2+=v2[i]**2
        m='{:.9f}'.format(m/(sqrt(l1)*sqrt(l2)))
    return m