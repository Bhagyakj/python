list1=[]
n=int(input("enter the number of elements: "))
print("elements are: ")
for i in range(n):
   i=int(input())
   if i<100:
      list1.append(i)
   else:
      list1.append('over')
print(list1)