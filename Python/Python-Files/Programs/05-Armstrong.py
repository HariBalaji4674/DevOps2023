print(153/10)
print(153//10)
print(153%10)

number  = 153
sum = 0
b = len(str(number))
rev = number

while number != 0:
    remainder = number%10
    sum = sum + remainder ** b
    number = number//10
print(sum)
print(rev)
if rev == sum:
    print("The Given Number is Armstromg")
else:
    print("The given Number is not Armstrong")


def armstrongNumber(number):
    sum = 0
    arms = number
    b = len(str(number))
    while number != 0:
        remainder = number % 10
        sum = sum + remainder**b
        number = number//10
    if arms == sum:
        print("{} : is Armstromg Number" .format(arms))
    else:
        print("{} : is NOT Armstromg Number" .format(arms))

armstrongNumber(153)
armstrongNumber(255)


# Algorithim Armstrong Number is sum of Cube of each number
# give the number
# Copy That number as another variable to compare
# initialize the Sum of number
# Traverse Through that number until number become zero
# take the remainder first
# Add initialized sum + remainder raised power of length of number
# then divide the number with 10 to get rid of last digit
# Compare both copied number and Sumed Number to get the result
