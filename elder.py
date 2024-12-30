class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
name1=input("enter name of first person1:")
age1=int(input("enter the age for person1:"))
person1=Person(name1,age1)
name2=input("enter name of second person2:")
age2=int(input("enter the age for person2:"))
person2=Person(name2,age2)
if person1.age>person2.age:
    print(f"{person1.name} is elder.")
elif person1.age<person2.age:
    print(f"{person2.name} is elder.")
else:
    print("both are same age")