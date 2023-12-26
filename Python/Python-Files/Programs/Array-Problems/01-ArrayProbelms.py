import array as arr

a = arr.array('i',[1,2,3,4,5])

for i in range(len(a)):
  print(a[i], end=" ")

# Replacing 2 with 7 will give = 1 7 2 3 4 5

a.insert(1,7)

for i in range(len(a)):
  print(a[i], end=" ")

# Array will not store Different Data Types
#a.append(3.5)
a.append(9)
for i in range(len(a)):
  print(a[i],end=" ")

# Accessing The elements

for i in a:
  print(i,end=" ")
print()
# Removing The elements with pop and Remove method
print(a)
a.pop(2) # Removes Number Based on Index Given
print(a)

a.remove(4) # removes the number provided if present else gives error
print(a)


# Slicing The array
for i in a[1:5]:
  print(i)

# Searching of Element

for i in range(len(a)):
  print(i ,"=",a[i])