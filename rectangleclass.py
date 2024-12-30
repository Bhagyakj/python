class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
l1=int(input("enter the 1st length:"))
b1=int(input("enter the 1st breadth:"))
r1=Rectangle(l1,b1)
print("area of 1st rectangle :",r1.area())
print("perimeter of 1st rectangle l:",r1.perimeter())
l2=int(input("enter the 2nd length:"))
b2=int(input("enter the 2nd breadth:"))
r2=Rectangle(l2,b2)
print("area of 2nd rectangle:",r2.area())
print("perimeter of 2nd rectangle:",r2.perimeter())
a1=r1.area()
a2=r2.area()
if a1>a2:
    print("area of 1st rectangle is higher")
elif a1==a2:
    print("area of both rectangles are equal")
else:
    print("area of 2nd rectangle is higher")