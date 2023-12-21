# Control Statements : Controlling the Statements 
# If the condition is repeating multiple times we use 

# There are three types of statements
# Conditional Statements --> if if-else elif
# Looping Statements --> for while
# Jumping Statements --> break continue

num1 = int(input("My Number1 is : "))
num2 = int(input("My Number2 is : "))
num3 = int(input("My Number is : "))
if(num1>num2):
    print(num1)
else:
    print(num2)

if(num1>num2):
    print(num1)
elif(num2>num3):
    print(num2)
else:
    print(num3)


if False:
    print("Hello World")
else:
    print("Hello India")

if 0 :
    print(num1)
else:
    print(num2)

# Even Or Odd Finding

if num1%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Ternary Operator

print("Even Number ") if num1>num2 else print("odd number")

# print("hello world") if num1>num2 print("hello india") elif num2>num3 else print("Hello Banglore")

weekno  = int(input("Enter the week Number : "))

if weekno == 0:print("Sunday")
elif weekno == 1:print("Monday")
elif weekno == 2:print("Tuesday")
elif weekno == 3:print("Wednesday")
elif weekno == 4:print("Thursday")
elif weekno == 5:print("Friday")
elif weekno == 6:print("Saturday")
else:print("Not Valid Number")