list1=[]
n=int(input("enter the number of elements: "))
print("elements are: ")
for i in range(n):
   element=int(input("{}:".format(i+1)))
   list1.append(element)
print("list=",list1)
pos=[num for num in list1 if num>0]
print("positive numbers=",pos)

