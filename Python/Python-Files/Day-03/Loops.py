# for i in range(2,10,2):
#     print(i)
# for i in range(10,0,-1):
#     print(i)
# for i in range(1,10,1):
#     if i == 8:
#         break
#     print(i)
# print("Program Exited")

# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

# Functions :

print(max(10,20,30))

print(10,20,50)

print(min(2,5,8,9,7,3,6,))

# Strings
name = "peddireddy"
print(name.upper())

s = str("")
print(type(s))

str = "welcome"
print(str*10)


#Slicing Concept

print(str[0:5])
print(str[2:])

# ord() and chr()

print(ord('A'))
print(chr(65))

print(max(25,45,36))
print(min(54,87,96))
# print(len(45,48,69))

print(len('peddireddy'))

# in and not in 


s = "welcome"
print("om" in s)

print("buddy" not in s)

#String Comparision

print("key" < "tie")
print("peddireddy" >= "hyderabad")
print("simple" >= "simple")

s = "peddireddy Hari vardhan reddy"

print(s.isalnum())
print("pedd".isalpha())
print("2012".isdigit())
print("first number ".isidentifier())
print(s.find("come"))
print(s.find("Hari"))


s = "peddireddy"

print(s.capitalize())
print(s.lower())
print(s.title())
print(s.casefold())
# print(s.center())

print(s.swapcase())
print(s.endswith('y'))


f = "peddireddy"
r = ""
for i in f:
    r = i + r
print(r)

for i in s[::-1]:
    print(i)