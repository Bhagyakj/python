list1=[]
n=int(input("enter the number of elements: "))
print("elements are: ")
for i in range(n):
   element=int(input())
   list1.append(element)
print("list=",list1)
new=[x for x in list1 if x%2!=0]
print("newlist=",new)