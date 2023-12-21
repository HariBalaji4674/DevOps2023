nums = [4,3,-25,9,2,42,45]
# print(nums)
# nums.sort()
# # print(num[])
# print(nums)

maximum = max(nums)
second_maximum = nums[0]
for i in range(0,len(nums)):
  if nums[i] > second_maximum and nums[i] != maximum:
    second_maximum = nums[i]

print(maximum)
print(second_maximum)


first_max =  max(nums[0],nums[1]) # [4,3,25,9,2,10,45]
second_max = min(nums[0],nums[1]) # [4,3,25,9,2,10,45]

for i in range(2,len(nums)):
  if nums[i] > first_max:
    second_max = first_max
    first_max = nums[i]
  elif nums[i] > second_max:
    second_max = nums[i]
  # print(nums[i]

  for i in 10:
    print(i)



print("first maximum number is",first_max)
print("second maximum number is ",second_max)