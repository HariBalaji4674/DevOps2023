
# nums = [2,7,11,15]
# target = 9
# class Solution:
#   def twoSum(self, nums: list[int], target: int) -> list[int]:
#     numMap = {}
#     n = len(nums)
#     for i in range(n):
#         numMap[nums[i]] = i
#     # Find the complement
#     for i in range(n):
#       complement = target - nums[i]
#       if complement in numMap and numMap[complement] != i:
#         return [i, numMap[complement]]

# c1 = Solution()
# print(c1.twoSum(nums,target))
#         # 7  = 9 - 2
#         # 7 in [2:0,7:1,11:2,15:3] and numMap[7] != 0
#         # return [0,7] No return

#         # 2 = 9 - 7
#         # 2 in [2:0,7:1,11:2,15:3] and numMap[2] != 1
#         # return [1,2] No Return

#         # -2 = 9-11
#         # -2 in [2:0,7:1,11:2,15:3] and numMap[-2] != 2
#         # return []

#         # -6 = 9-15
#         # -6 in [2:0,7:1,11:2,15:3] and numMap[-6] != 3
#         # return []

# class solution:
#   def sum(self,nums,target):
#     seen = {}
#     for i,num in enumerate(nums):
#       if target - num in seen:
#         return [seen[target-num],i]
#       elif num not in seen:
#         seen[num] = i

# target = 9
# nums = [2,7,11,15]
# vau = solution()
# print(vau.sum(nums,target))



# n = [10,20,30,40,50]
# n1 = len(n)
# for i in range(n1):
#   print(i)
nums = [2,7,11,15]
for i,nums in enumerate(nums):
  print(i)
  # print(nums)