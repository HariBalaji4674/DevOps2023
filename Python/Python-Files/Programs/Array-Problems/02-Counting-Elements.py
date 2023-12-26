import array as arr
from numpy import *

# Counting Elements in Array

# a = arr.array('j', [ 2,4,6,8,9,3 ])
a = arr.array('i',[1,2,3,4,5,5,3,7,5,6,8,9])
for i in range(len(a)):
  print(i)

print("Count Of Elements")
count = a.count(3)
print(count)

print(a)
a.reverse()
print(a)

# a.sort()
# print(a)

# Extend is function used to add more elements at the end
# Used to attach An item from iterable to the end of array

a.extend([23,24,34,56,76,23,43])
print(a)

arr = array([[23,24,25],[27,28,29]])
print(arr)