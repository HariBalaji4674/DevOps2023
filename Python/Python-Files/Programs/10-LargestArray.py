Arr = [25,85,64,75,23,12]

max = Arr[0]

for i in range(1, len(Arr)):
    if Arr[i] < max:
        max = Arr[i]

print(max)

