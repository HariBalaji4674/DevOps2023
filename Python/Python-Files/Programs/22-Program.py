'''
Create a List
then cube it with each number

'''

list = [1,2,3]
list1 = []

for i in list:
  # list1[i] = list[1]*list[i]*list[i]
  list1.append(i*i*i)
  print(i)
print(list1)

for i in list:
  for j in list1:
    print(i,j)

# Lambda Function

a = 10
x = lambda a : a+10
print(x(a))

y = lambda a : a*a*a
print(y(2))

# list1 = [1,2,3]
# resu  = list(map(lambda x : (x , x**3),list1))

# print(resu)



list1 = [1, 2, 5, 6]
res = list(map(lambda x: (x, x**3), list1))
print(res)