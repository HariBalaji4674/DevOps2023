def fibonacci(number):
    if number<0:
        print("Incorrect number")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number-1)+fibonacci(number-2)

print(fibonacci(10))

# Sum of previous two numbers

# number1 =
# number2 =
# number3 = number1+number2

