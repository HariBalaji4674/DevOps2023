nums = [2,7,11,15]
target = 9

'''
what is an array in python
Functions annotations

'''
def velocity(s,t) ->'mph':
return (s/t)
print(velocity(200,10))

def f(self,s:'str') -> 'bool':
pass

nums = [2,7,11,15]
target = 9
class solution:
def twosum(self,nums,target):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

c1 = solution()

print(c1.twosum(nums,target))

nums = [2,7,11,15]
target = 9
class solution:
def twosum(self,nums:list[nums],target: int) -> list[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [i,j]

c1 = solution()

# print(c1.twosum(nums,target))

# numMap = {} # Empty Dictionary
# n = len(nums)

# for i in range(n):
#     numMap[nums[i]] = i

# print(numMap) # {2: 0, 7: 1, 11: 2, 15: 3}

# nums = [2,7,11,15]
# target = 9
# for i in range(n):
#     # lisNum = set({ })
#     lisNum = []
#     complement = target - nums[i]
#     lisNum.append(complement)
#     print(numMap[complement])
#     print(lisNum)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}
        n = len(nums)

        # Build the hash table
        for i in range(n):
            numMap[nums[i]] = i

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

            7  = 9 - 2
            7 in [2:0,7:1,11:2,15:3] and numMap[7] != i

