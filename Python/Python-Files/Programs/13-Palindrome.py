# Palindrome
'''
integer x
if x = palindrome
return true
else
return false

What is palindrome:
- A numebr should be same from bothe the sides
121 323 434
'''
# x = 121
# sum = 0
# def palind(self,x):
#   num = x
#   for i in range(0,len(str(x))):
#     rem = num%10
#     sum = sum*10 + rem
#     num = num//10
#   if sum == x:
#     return True
#   else:
#     return False
print("Om Namo Narayanayanaya")
# print(palind(121))
# print(len(str(x)))

class Solution:
  def ispalnidrom(self,x):
    if x<0:
      return False
    reversed_num = 0
    temp = x
    while temp != 0:
      digit = temp % 10
      reversed_num = reversed_num * 10 + digit
      temp = temp//10

    return reversed_num == x
obj = Solution()
print(obj.ispalnidrom(464))


class Solution1:
  def twosum(self,list1,target):
    seen = {}
    for i,num in enumerate(list1):
      if target - num in seen:
        return [seen[target-num], i]
      elif num not in seen:
        seen[num] = i
obj2 = Solution1()
list1 = [2,7,11,15]
target = 9
print(obj2.twosum(list1,target))

sum = 0

class Solution3:
  def palindrome(self,num):
    if num<0:
      return False
    x = num
    sum = 0
    while x != 0:
      digit = x % 10
      sum = sum*10 + digit
      x = x//10

    return sum == num

obj4 = Solution3()
print(obj4.palindrome(121))

num = 10
print(num // 10) # Gives Intiger Number
print(num / 10) # Gives Float Number
print(num % 10) # remainder

'''
given number

initialize the number
copy the number
loop unitl the number == 0
 get the remainder
 add it to the sum of number by multiply by 10
 get the quotient

'''
num = {}
sum = [2,7,5,6,7,9,12,34,65,55]
for i in range(10):
  num[i] = sum[i]
print(num)

# nums = 12
# li = num.keys
# for nums in li:
#   if nums == num:
#     print("true")
#   else:
#     print("false")




