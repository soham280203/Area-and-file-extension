import math #import math for including math library
pie=math.pi #math. funtn returns whole value of pi inside pie
a=float(input('Input the radius of the circle:')) #asks user to enter radius of circle
area=pie*a*a
print("The area of the circle with radius %0.1f is %0.16f"%(a,area))
