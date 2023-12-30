list1 = [2,3,5,6,8]
list2 = [8,4,9,4,10]

temp = list1[0]
list1[0] = list1[-1]
list1[-1] = temp

print(list1)

