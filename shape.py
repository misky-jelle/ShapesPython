# It has a method area that returns the area (A) of the circle using the formula A=πr


from cmath import pi
import math


class Circle:
  def __init__(self,r):
    self.r=r
    
 
  def area(self):
        Area = math.pi* self.r
        return Area

# It has a method to calculate circumference (c) using the formula C=2πr
  def circumfrence(self):
     circumfrence = 2*math.pi* self.r
     return circumfrence
        
# Class Square
# A Square instance accepts the attribute side (a)
class square:
    def __init__(self,a):
        self.a=a


# It has method area that returns the area (A) of the square using the formula A=a2
    def Area(self):
     A=self.a*self.a
     return A

    #  It has a method to calculate the perimeter (P) of the square using the formula P=4a
    def permiter(self):
       P=4*self.a
       return P

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
class rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
        A=self.w*self.l
        return A


# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
    def perimeter(self):
        P=2*self.l*self.w
        return P

# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
#  has a method to calculate the surface area (A) using the formula A=4πr2

class sphere():
    def __init__(self,r):
           self.r=r
    def surface_area(self):
        A=4*pi*self.r*self.r
        return A
        # It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)
    def volume(self):
        V=4/3(pi*self.r*3)
        return V



