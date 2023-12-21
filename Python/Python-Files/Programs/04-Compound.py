
def ci(principle,rate,time):
    if(principle == 0):
        return principle
    else:
        amount = principle*(pow(1+rate/100,time))
        return amount - principle

print(ci(100000,25,5))

sum  = pow(3,4)
print(sum)

principle = 100000
rate = 3
time = 4

amount = principle*(pow(1+rate/100,time))
ci = amount-principle
print(float(ci))

round(ci,2)
print(ci)

print("%.2f" % round(ci,2))

print("{:.2f}" .format(ci))

print("{:.2f}" .format(round(ci,2)))
print("{:.4f}" .format(ci,2))
print("round of ci : {:.5f}" .format(ci))

# a = 13.946
# print(a)
# 13.946
# print("%.2f" % a)
# 13.95
# round(a,2)
# 13.949999999999999
# print("%.2f" % round(a, 2))
# 13.95
# print("{:.2f}".format(a))
# 13.95
# print("{:.2f}".format(round(a, 2)))
# 13.95
# print("{:.15f}".format(round(a, 2)))
# 13.949999999999999

