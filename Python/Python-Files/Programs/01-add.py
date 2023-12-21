num1 = 5
num2 = 3

sum = num1 + num2

print(sum)

print("*********************")

num3 = int(input("Please Enter a num3 : "))
num4 = int(input("enter a number4 :"))

sum  = num3 + num4

print(sum)

print(max(num3,num4))

print("*************************")

def maximum(a,b):
    if a>b:
        print(a)
    else:
        print(b)

a = int(input("Enter a Value : "))
b = int(input("Enter b Value : "))
maximum(a,b)

print("**********************")

print("Factorial Of Number")

def fact(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n*fact(n-1)

factorial  = int(input("Please Enter the Factorial Number : "))

print("Factorial of {} is : ".format(factorial),fact(factorial))


