print("hello world")

class Myclass:
    def name(self):
        print("peddireddy")
        pass
    def sum(self):
        print("simple")
        pass

name = Myclass()   #This is Object and assigning to variable name

name.name()
name.sum()


# Passing Arguments to the Function

class shop:
    def ownFun(self):
        pass
    def shopName(self,name1):
        print("My shop Name is : ",name1)
    def streetName(self,name1,name2):
        print("Street Name is : ", name1)
        print("Street Name 2 is : ", name2)

shopname = shop()
shopname.shopName("BigBazaar")

fun1 = shop()
fun1.shopName("D-Mart")
fun1.ownFun()
fun1.streetName("Shivaji Nagar","Anna-Nagar Main Road")

# Example -- 2

class sumOfNum:
    def sum(self):
        pass
    def sum1(self,num1,num2):
        sum = num1+num2
        print(sum)
    @staticmethod
    def sum2(num1,num2,num3):
        sum = num1+num2+num3
        print(sum)

sumFun = sumOfNum()

sumFun.sum()
sumFun.sum1(10,20)
sumFun.sum2(10,20,30)

# There are 2 type of Methods in class
# Static method --> we can call directly
# Instance Method  --> We can call through object only

class pgType:
    def pgName(self):
        print("My Pg name is Sri Sathya Durga pg")
        pass
    def roomNo(self, num1,num2,num3):
        print("my Number 1 :{}, My Number2 is : {},my Number is Number {} ".format(num1,num2,num3))
    @staticmethod
    def roomMates(name1,name2,name3):
        print("My Name is :  {} , My Friend1 Name is:  {}, My friend name3 is :  {} " .format(name1,name2,name3))


pgType.roomMates("hari","akhila","harsha")

func = pgType()
func.pgName()
func.roomNo(10,20,30)


# Variables Inside the class

class variables:
    def var1(self):
        print("Printing the Variables")
        pass
    name1 = "peddireddy"
    name2 = "hari vardhan"
    def names(self):
        print(self.name1,self.name2)

        
objClass = variables()
# print(objClass.names())
# print(objClass.var1())
objClass.names()
objClass.var1()


class calculator:
    number1 = 10
    number2 = 20
    number3 = 30
    def add(self):
        print(self.number1+self.number2+self.number3)
        pass

    @staticmethod
    def add1(number1,number2,number3):
        print(number1+number2+number3)

    @staticmethod
    def sub(number1,number2):
        print(number1-number2)

    @staticmethod
    def mul(number1,number2,number3):
        print(number1*number2*number3)
    
myClass = calculator()
myClass.add()
calculator.add1(10,20,30)
calculator.sub(30,20)
calculator.mul(2,3,4)



i = 20
j = 30

class myClass:
    k = 25
    l = 30
    def add(self):
        print(self.k,self.l)
        print(i,j)
    def localvar(self,a,b):
        print(i,j)
        print(self.k,self.l)
        print(a,b)
    def globalvar(self,i,j):
        print(i,j)
        print(self.k,self.l)
        print(globals()['i'],globals()['j'])

# Creating the Multiple Objects for a class

obj1 = myClass()
obj2 = myClass()
obj3 = myClass()
obj4 = myClass()

# Constructor

class myClass:
    def __init__(self):
        print("This is Constructor Calling")
    def m1(self):
        print("Hello this not constructor")

m1 = myClass()
m1.m1()


# Constructer with Parameters

class number1:
    def __init__(sef,a,b):
        print(a,b)
mc = number1(10,20),












# print("My name is :",name ,"My Age is :",age, "My salary is :",salary)


# print("Name is : %s -- Age is : %d --  My Salary is : %g " %(name,age,salary))

# print("My Name is : {}  Age is : {}  My Salary is {}" .format(name,age,salary))
