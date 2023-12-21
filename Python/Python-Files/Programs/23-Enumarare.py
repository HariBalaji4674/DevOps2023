x = ("apple","banana","Grapes")
y = enumerate(x)
for i in x:
  print(i)
# print(y)

import json
from turtle import ycor
x = '{"name":"peddireddy","section":"23","gender":"male"}'

y = json.loads(x)
print(y["name"])

x = {"name":"peddireddy","section":"23","gender":"male"}
y = json.dumps(x)
print(y)