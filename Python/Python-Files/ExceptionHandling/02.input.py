import os
number = input("Enter The Number : ")
print("You have Given The number : ", number)

print(os.listdir)
folders=input("Please Provide List of folders Names spaces in between : ").split()

print(folders)

for i in folders:
    files = os.listdir(i)
    print(files)