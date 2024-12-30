print("\nSQUARE")
a=int(input("enter the side of square: "))
square=lambda a:a*a
print("Area of square=", square(a))
print("\nRECTANGLE")
l=int(input("enter the length of rectangle: "))
b=int(input("enter the width of rectangle: "))
rectangle=lambda l,b:l*b
print("Area of rectangle=",rectangle(l,b))
print("\nTRIANGLE")
h=int(input("enter the height of triangle: "))
c=int(input("enter the base of triangle: "))
triangle=lambda h,c:.5*h*c
print("Area of triangle=",triangle(h,c))
