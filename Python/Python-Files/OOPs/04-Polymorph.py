import abc

'''
Polymorphism : Poly Means Many Form
Duck Typing
Methods Overriding
Method Overloading
Operator Over Loading
'''
class Ducktypinh:
    def main(self):
        print("This is Main Methdod ")

'''
Abstract Methods
import abc
@abstractmethod
for every method which need to make the method to Abstract

Iterator:

'''
nums = [1,23,4,5,6,7]
it = iter(nums)
print(it.__next__())


class Top100:
    def __init__(self): # It will call by default when object is created
        self.num = 1
    def __next__(self):
        if self.num <= 10:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration
    def __iter__(self):
        return self


c1 = Top100()
for i in c1:
    print(i)
'''
Generator: It will create a Iterator
yield will give the iterator
'''
def topten():
     n = 3
     while n <= 10:
         sq = n*n
         yield sq
         n = n+1

values = topten()
for i in values:
    print(i)
