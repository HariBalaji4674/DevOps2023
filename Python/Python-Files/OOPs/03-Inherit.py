'''
Inheritance : Copying behaviour and Attributes from Parent to Child
Super Keyword is used to use Super Class Constructor

'''
class a:
    def __init__(self):
        print("This is Class a Init method ")
    def method1(self):
        print("Feature 1 Working")
    def method2(self):
        print("Feature 2 Working")

class b:
    def __init__(self):
        super().__init__()
        print("This is Class-B init method ")
    def method3(self):
        print("Feature 3 Working")
    def method4(self):
        print("Feature 4 Working")

obj1 = b()
obj1
# print(obj1.method1())
# print(obj1.method2())
print(obj1.method3())
print(obj1.method4())


class c(a,b):
    def __init__(self):
        super().__init__()
        print("This is class-c init method")

obj2 = c()



