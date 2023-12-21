# Tuple List Program

from ctypes import sizeof
from re import T
import sys


Tuple1 = (1,2,3,4,5,6)
Tuple2 = (4,7,8,12,45)

print(len(Tuple1))

print(str(sys.getsizeof(Tuple1)))
print(Tuple1.__sizeof__())

list1  = ('apple', 'banana', 'cherry')

# print(list1)

y = enumerate(list1)
print(list(y))
