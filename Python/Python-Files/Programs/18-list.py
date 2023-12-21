nums = [23,45,67,98,24,10]
#range(start,stop,step)
n = len(nums)
for i in range(n-1,-1,-1):
  print(nums[i],end=" ")

print(" ")
arr = [100,10,5,25,35,14]
n = 11
n1 = len(arr)
sum = 1
for i in range(0,n1):
  sum = sum*arr[i]
print(sum%n)

# Largest element in array

max = arr[0]
for i in range(0,n1):
  if arr[i] > max:
    max = arr[i]
print(max)

# Monotone Increasing or Mnotone Decreasing
arr = [100,10,5,25,35,14]
n = len(arr)
def monotone(arr,n):
  for i in range(0,n):
    for j in range(i+1,n):
      if arr[i] >= arr[j]:
        # return arr[i]
        return True
      else:
        return False
arr = [100,10,5,25,35,14]
n = len(arr)

print(monotone(arr,n))
print(arr.reverse())
arr.sort()
print(arr)
'''
Python Collections

List = [1,2,3,4,5,6]
Set = (1,2,3,4,5)
Tuple = (1,2,3,4,5,6)
Dictionary = {1="peddireddy", 2="reddy"}

'''