a = [10,20,30,40,50]
print(a)

b = ["apple","banana","cherry","donle","elegant","fish"]
print(b)

print(b[-1])
print(b[0])
print(b[0:3])
print(b[1:4])
print(b[2] == "compile")
b[2] = "compile"
print(b)

for i in b:
    print(i)

if "compile" in b:
    print(b)
else:
    print("item does not present")

print(len(b))


t = ("apple","banana","brinjal","coconut")
print(t)

t[1] = "bobby" # Type does not allow assignment 
print(t) # Tuple is Immutable Value 

# We cannot do crud operations on tuple 
# Tuple is more secure than List
# we can change tuple into list and do some modifications and again change the list to tuple

