
def prime(number):
    for i in range(0,number):
        if i%2 == 0:
            print(i)
prime(20)

def prime1(x,y):
    print_list = [ ]
    for i in range(x,y):
        if i==0 or i==1:
            continue
        else:
            for j in range(2,int(i/2)+1):
                if i%j == 0:
                    break
            else:
                print_list.append(i)
    return print_list

print(prime1(4,24))

# what is prime number :
#A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}.
# Dividend = Divisor x Quotient + Remainder.
print(2%3)
print(4%5)
print(7%4)


def divisiors(num1,num2):
    list = [ ]
    for i in range(num1,num2):  # 4
        if i==0 or i==1:
            continue
        else:
            for j in range(2,i): # 2,3,4
                if i%j == 0:
                    break
            else:
                list.append(i)
    return list

print(divisiors(3,67))

def prime2(start,end):
    list1 = [ ]
    flag = 0
    for i in range(start,end):
        for j in range(2,i):
            if i%j==0:
                flag = 1
                break
            else:
                flag=0
        if flag==0:
            list1.append(i)
    return list1

print(prime2(0,25))

