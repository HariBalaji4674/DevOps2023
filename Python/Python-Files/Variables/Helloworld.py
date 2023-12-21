name = "peddireddy hari vardhan reddy"

name1  = name.split(" ")
print(name1)

name2  = name.upper()
print(name2)

name3 = name.lower()
print(name3)

name4=name.replace("peddireddy","annampappu")
print(name4)

import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")


name="Peddireddy"
print(name)

a =10
b=20
def addition():
    return (a+b)

print(addition())

def substraction():
    a = addition()
    b = 10
    return (a-b)

print(substraction())