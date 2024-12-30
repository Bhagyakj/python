list1=[]
c=0
n=int(input("enter the number of words: "))
print("words are: ")
for i in range(n):
   i=(input())
   list1.append(i)
for x in list1:
    for j in x:
        if 'a' in j.lower():
            c=c+1
print(" the occurance of 'a' is:",c)

