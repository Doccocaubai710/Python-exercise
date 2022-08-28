def remove_duplicates(s):
    previous_value=None
    newlist=[]
    for i in x:
      if i!=previous_value:
        newlist.append(i)
        previous_value=i
    print(newlist)
x=[1,0,0,2,3]
remove_duplicates(x)