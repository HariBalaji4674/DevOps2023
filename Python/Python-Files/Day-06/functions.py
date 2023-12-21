def add(a ,b):
    print(a+b)
def hello():
    print("helloworld")
def kill(hello,world):
    print(hello+world)
def myName(name):
    print("hello", name)

add(10,20)
hello()
kill(20,30)
myName("peddireddy")

#Local Variable
def name():
    a = 20
    b = 25
    print(a+b)
# print(a)
# print(name(a))

# Global Variables
a = 30
b = 40

def number():
    print(a+b)

number()
print(a)



# Types of Arguments:

def myFunc(i,j):
    print(i,j)
myFunc(20,30)
myFunc(j=40,i=70)

def nam(i,j=20):
    print(i,j)
nam(i=100,j=300)

def numm(i,j=50):
    print(i,j)
numm(250)

def greet(name,timings):
    print("Hello",name,"Welcome to TCS RMG", timings)

greet('peddireddy','akhila')