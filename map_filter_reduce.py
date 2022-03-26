#-----[ Map ]-----------------
#fruits = ['apple', 'banana', 'cherry'] # list
fruits = ('apple', 'banana', 'cherry') # tuple

x = map(lambda x: len(x), fruits)

print(x) # unreadable x value

#convert the map into a list, for readability:
fruitslist = list(x)
print(fruitslist)

# other solution------------
def myfunc(a):
  return len(a)

x = map(myfunc, fruits)
print(list(x))

#-----------
l1 = [2,3,4,5,6]
l2 = list(map(lambda x: x*2, l1)) #dubbling the l1 all items
print(l2)


#-----[ Filter ]-----------------
l3 = [2,3,4,5,6]
filtering_the_l3 = list(filter(lambda x: x%2 ==0,l3))
print(filtering_the_l3)

#-----[ Reduce ]-----------------
from functools import reduce

sum_items = [2,3,4,5,6]

total = reduce(lambda x, y: x+y, sum_items)
print(total)

#---------
def add(x, y):
   return x+y

total2 = reduce(add, sum_items)
print(total2)