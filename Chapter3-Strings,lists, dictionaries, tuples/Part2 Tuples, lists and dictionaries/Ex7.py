def sort_students(l):
    x=sorted([(v,k) for k,v in l])
    y=[(v,k) for k,v in x ]
    return y
print(sort_students([('John', 9.75), ('Max', 9.5), ('James', 9.5), ('Henry', 8.5)]))    