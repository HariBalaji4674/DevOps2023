def factorial(n):
    if ( n == 0 or n == 1 ):
        return 1
    else:
        return n*factorial(n-1)

number = int(input("Please Enter the Number : "))
print("Factorial of {} is : ".format(number),factorial(number))


def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)

number1 = int(input("Please Enter the Number : "))
print("Factorial of {} is : ".format(number1),fact(number1))
