from numpy import maximum


list1 = [87,25,76,34,98]

maximum = list1[0]
for i in list1:
  if i < maximum:
    maximum = i
print(maximum)

list1.sort()

print(list1[0])


