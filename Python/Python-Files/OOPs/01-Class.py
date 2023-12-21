class Item:
    pass

item1 = Item()
item1.name = 'phone'
item1.price = 100
item1.quantity = 5

'''
Functions
Modules
Procedural Programming language

OOPs Concepts --> Object Programming Language:
-----------------------------

Object Have 2 Things: Attribute & Behaviours

Attribute ==  data
behaviour ==  how data works
Class ==  design of objects (Blue-Print)
Variables == store somethings
methods ==  where to use those behaviour

Attributes == Variables in Class
behaviour  == methods in class

__init__(self) will be called Automatically when we create object/Constructor


__init__(self)
c1 = contructor() --> This is Constructor

Size of the Ovejct is depends on the No of Variables
Who calculates the memory is called Constructor

Why Self Is needed:
    -


'''
class computer:
    def config(self):
        print("i5 Configuration ")

comp1 = computer()
print(comp1.config())

class main:
    def __init__(self,name,age):
        self.name = name
        self.age = age

maiFun = main('peddireddy',23)
print(maiFun.age)
print(maiFun.name)

class car:
    def __init__(self):
        self.name = "Skoda"
        self.number = "12-10-23"
        self.driver = True
    def __init__(self):
        self.number = "13-12-23"
    def __init__(self,number):
        self.number = number

c1 = car("18-12-23")
c2 = car("18-12-23")
c3 = car("18-12-23")

print(c1.number)

c1.number = "15-12-23"

print(c1.number)

print(c2.number)

# c3.number = "18-12-2023"

print(c3.number)

class compare:
    def __init__(self):
        self.age = 28
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False

obj = compare()
obj2 = compare()
obj.age = 23
obj2.age = 23

if obj.compare(obj2):
    print("Ages are same")
else:
    print("ages are different")



'''
In memory we have namespace
 - Class Namespace
 - Object/Instance Namespace
Instance Variables
Class Variables
Global Variables

Methods: Behaviour
    Instance Method
    Class Method
    Static Methods
Instance Methods: Because it works with Instance/Objects
    Accessor : Only Acces the values
    Mutators : Can Change and set the values
'''
#Instance Method/Object Method -- Values should be assigned based on Objects
class student:
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

i1 = student(250,350,650)
i2 = student(450,120,560)

print(i1.avg())

#Class Method : Variables should be passed via class varibales
class Classmethod:
    school = "shantinikethan"
    @classmethod
    def getschool(cls):
        return cls.school

print(Classmethod.getschool())

#Static Method : passing Variables Statically

class Staticmethod:
    @staticmethod
    def sttemth():
        print("This is static Methods")

Staticmethod.sttemth()
# print(Staticmethod.sttemth())

