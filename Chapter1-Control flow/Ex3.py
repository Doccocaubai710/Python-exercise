distance=float(input())
speed=float(input())
if (distance<=2):
  price=12000
else: 
  time=(distance-2)/speed
  price=12000+time*350+(distance-2)*3500
print('{:.2f}'.format(price))  