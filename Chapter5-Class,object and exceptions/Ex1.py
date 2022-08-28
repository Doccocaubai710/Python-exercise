from math import sqrt
from math import pi


class Figure:
    def perimeter(self):
        pass

    def area(self):
        pass
class LengthException(Exception):
    pass
class InvalidTriangleException(Exception):
    pass

class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            if width>0 and height>0:
                self.width=width
                self.height=height
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e))+' was raised')
    def perimeter(self):
        return (self.width+self.height)*2
    def area(self):
        return self.width*self.height
class Circle(Figure):
    def __init__(self,r):
        try:
            if r>0:
                self.r=r
            else:
                raise LengthException
        except LengthException as e:
            print(print(str(type(e))+' was raised'))
    def perimeter(self):
        return 2*pi*self.r
    def area(self):
        return pi*self.r*self.r

class Triangle(Figure):
    def __init__(self,a,b,c):
        try:
            if (a>0) and (b>0) and (c>0):
                if (a+b)>c and (b+c)>a and (c+a)>b:
                    self.a=a
                    self.b=b
                    self.c=c
                else:
                    raise InvalidTriangleException
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
        except InvalidTriangleException as e:
            print(str(type(e)) + ' was raised')

    def perimeter(self):
        return self.a+self.b+self.c
    def area(self):
        a,b,c=self.a, self.b, self.c
        return sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b)/16)
rec = Rectangle(1, 2)
tri = Triangle(3, 4, 5)
print(rec.perimeter())
print(tri.area()) 