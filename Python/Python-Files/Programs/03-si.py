print("si")

def si(principle,time,rate):
    if( principle == 0 or time == 0 or rate == 0):
        return principle
    else:
        return (principle*time*rate)/100

principle = int(input("Please Enter Principle Amount : "))
time = int(input("Please Enter time taken : "))
rate = int(input("Please Enter Rate Of Intrest : "))
print(" Simple Intrest for {},{},{} : is {}".format(principle,time,rate,si(principle,time,rate)))
