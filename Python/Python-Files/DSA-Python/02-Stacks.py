# Implementing stack using list
# Implements:
# List & Modules basic operayions are Push and Pop
# Push --> Append add the end of the list
# Pop --> Remove end of list

stack = []
stack.append(20)
print(stack)
stack.append(52)
print(stack)
stack.append(45)

print(stack)
stack.append(35)

print(stack)

stack.append(46)

print(stack)

stack.pop(2)
print(stack)


stack = []
def push():
    element = input("Enter the element : ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        element = stack.pop()
        print("Removed element is :", element)
        print(stack)

while True:
    # print("Please Select The operation Choice 1,Choice 2 Choice 3 ")
    choice = int(input("Enter The Choice : "))
    if choice == 1:
        push()
    elif choice == 2 :
        pop()
    else:
        print(stack)
        break










































