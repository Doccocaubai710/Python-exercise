
# tree= []
# n = int(input())
# while n >1:
#     tree.append(input().split())
#     n -=1

# dic = dict()
# for x,y in tree:
#     dic[y]= 0
# for x,y in tree:
#     dic[x]= dic.get(y,0) +1

# ak = sorted(list(dic.items()),key= lambda x: x[0])
# for x, y in ak:
#     print(x,y)



family_tree= []
n = int(input())
while n > 1:
    family_tree.append(input().split())
    n -=1

family_dict = dict()
for _,lname in family_tree:
    family_dict[lname]= 0
for fname,lname in family_tree:
    family_dict[fname]= lname


def findAncestor(fanme,family_dict):
    """
    INPUT: 
        fname: first name (example A)
        family_dict: dictionary of family where key is first name
            and value is last name (first name of direct ancestor)
            in case of the most ancestor, the value is the height 0.
    """
    if str(family_dict[fanme]).isnumeric():
        return family_dict[fanme]
    family_dict[fanme]= 1+ findAncestor(family_dict[fanme], family_dict)
    return family_dict[fanme]


for fname in family_dict:
    findAncestor(fname,family_dict)
for fname, height in sorted(family_dict.items()):
    print(fname, height)
"""
n = int(input())

first = [tuple(input().split()) for i in range(n-1)]
sons = [first[i][0] for i in range(n-1)]
dads = [first[i][1] for i in range(n-1)]

h = dict()
for dad in dads:
    if dad not in sons:
        h[dad] = 0

for j in range(n-1):
    for i in range(n-1):
        son = sons[i]
        dad = dads[i]
        if dad in h:
            h[son] = h[dad] + 1


listh = [(name, h[name]) for name in h]
listh.sort()
for ele in listh:
    print(*ele)




"""




