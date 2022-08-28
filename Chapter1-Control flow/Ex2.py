import math


ax, ay, bx, by, cx, cy= [float(i) for i in input().split()]
L1=math.sqrt((ax-bx)**2+(ay-by)**2)
L2=math.sqrt((ax-cx)**2+(ay-cy)**2)
L3=math.sqrt((bx-cx)**2+(by-cy)**2)
if (L1+L2>L3) and (L1+L3>L2) and (L2+L3>L1):
    if (L1**2+L2**2<L3**2) or (L1**2+L3**2<L2**2) or (L2**2+L3**2<L1*2):
        print('Obtuse triangle')
    elif (L1**2+L2**2==L3**2) or (L2**2+L3**2==L1**2) or (L1**2+L3**2==L2**2):
        print('Right triangle')
    elif (L1**2+L2**2>L3**2) and (L2**2+L3**2>L1**2) and (L1**2+L3**2>L2**2):
        print('Acute triangle') 
else:
    print('Straight line')     