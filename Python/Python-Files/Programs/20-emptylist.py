''' removing empty list in the list'''
# Using List Comprehension
list1 = [23,20,[],45,67,[],89,[],34,29,[]]
lst = []
print(list1)
for i in list1:
  if i != []:
    lst.append(i)
    print(i, end=" ")
print(lst)

''' Using Filter() Method '''
list1 = [23,20,[],45,67,[],89,[],34,29,[]]

str(list1)

result = list(filter(None, list1))

print(str(result))

'''Using Function '''

def removingEmptyList(list_items):
  new_list= []
  for element in list_items:
    if element:
      new_list.append(element)
  return new_list

list_items = [23,20,[],45,67,[],89,[],34,29,[]]

lsit = removingEmptyList(list_items)
print(f"thisis new list {lsit}")
print(lsit)

'''Using List Map Join Replace '''
list1 = [23,20,[],45,67,[],89,[],34,29,[]]

print(list1)

x = list(list1)
print(x)

y = list(map(str,list1))
print(y)
z = " ".join(y)
print(z)

a = z.replace("[]","")
print(a)
# a=list(map(int,a))
# print(str(a))

# List Comprehension

# newList = [x for x in a if x%2 == 0 ]
# print(newList)

''' Joining List '''