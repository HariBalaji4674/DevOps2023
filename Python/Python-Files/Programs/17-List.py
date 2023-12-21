'''
num = 0
while num < 10:
  print(num, end=" ")
  num = num+1

def splitArr(arr,n,k):
  for i in range(0,k):
    x = arr[0]
    for j in range(0,n-1):
      arr[j] = arr[j+1]
    arr[n-1] = x

arr = [25,12,11,36,45,65,78,32]
n = len(arr)
k = 2

splitArr(arr,n,k)
for i in range(0,n):
  print(arr[i],end=" ")

def splitarray(arr,n):
  for i in range(0,int(n/2)):
    x = arr[0]
    for j in range(0,n-1):
      arr[j] = arr[j+1]
    arr[n-1] = x
arr = [11,22,33,44,55,66,77,88]
n = len(arr)

splitarray(arr,n)
for i in range(0,n):
  print(arr[i],end=" ")
'''
arr = [11,22,33,44,55,66,77,88]
print(arr[::])
b = 2
c = arr[:b]
print(c)
d = arr[b:]
print(d+c)

