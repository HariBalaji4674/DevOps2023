file = open("C:/Users/KRISHNA HARI/NewLearning/Python-Shell-Files/Python-Files/Day-10/file.txt",'w')

file.write("This is first Statement \n ")
file.write("This is second Statement \n ")
file.write("This is Third Statement \n ")
file.write("This is Fourth Statement \n ")
file.close()

print("Added new Files")

file1=open("C:/Users/KRISHNA HARI/NewLearning/Python-Shell-Files/Python-Files/Day-10/file.txt",'r')

# print(file1.readline(1))

for i in file1.readline(1):
    print(i) 
print()


