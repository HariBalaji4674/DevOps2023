# Pattern Problems
'''
print("*")

for i in range(1,10):
  print(i ,"= *")

# Function Parameter:

def Func(n):
  for _ in range(n):
    for _ in range(i):
      print("*", end=" ")
    print()

n = 12
Func(n)

def Func(n):
  for i in range(n):
    for _ in range(i+1):
      print("*", end=" ")
    print()

n = 5
Func(n)

def Func(n):
  for i in range(n,-1,-1):
    for _ in range(i):
      print("*",end=" ")
    print()
n = 5
Func(n)

def Func(n):
  for i in range(n):
    for _ in range(i,n):
      print("*",end=" ")
    print()
n = 5
Func(n)


print(1,2,3,4,5, end=" ")
'''
# Increasing i Values outside the hence gives 1 2,2 3,3,3
for i in range(5):
  for _ in range(i):
    print(i,end=" ")
  print()
i = i+1

# Increasing i Values inside the  loop Gives 1 2,3 3,4,5 4,5,6,7

for i in range(5):
  for _ in range(i):
    print(i,end=" ")
    i = i+1
  print()

# Increasing i Values outside the loop hence gives 1 2,2 3,3,3
for i in range(5):
  for j in range(i+1):
    print(j,end=" ")
  print()
j = j+1

# Increasing i Values inside the loop Gives 1 2,3 3,4,5 4,5,6,7

for i in range(5):
  for j in range(i+1):
    print(j,end=" ")
    j = j+1
  print()


