list = [2,3,4,7,5]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i] >= list[j]:
            list[i],list[j] = list[j],list[i]
print(list)