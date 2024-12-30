from functools import reduce
c=reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda x:x<=4,[1,2,3,4,5,6,7])))
print(c)