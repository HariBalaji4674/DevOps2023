list1 = [23,20,45,67,89,34,29]

minimum = list1[0]

print(minimum)

for i in list1:
  if i < minimum:
    print(i)

'''
Clearing the list using different methods
using clear()
using *=0
using del
using pop()
using slicing
reinitializing the list

'''
list1 = [23,20,45,67,89,34,29]
list1.clear()
print(list1)


list1 = [23,20,45,67,89,34,29]
list1*=0
print(list1)

list1 = [23,20,45,67,89,34,29]
list1.pop()
print(list1)
while (len(list1) != 0 ):
  list1.pop()
print(list1)

list1 = [23,20,45,67,89,34,29]
del list1[:]
print(list1)


list1 = [23,20,45,67,89,34,29]
lst = list1[:0]
print(lst)

