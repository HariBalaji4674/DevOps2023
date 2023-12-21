# Constructor & self
class Computer:
    pass

c1 = Computer()

print(id(c1))

# Size of An object
# Who Allocates the memory
# Depends on the no of varaibles and size of each variable the memorywill allocate in the heap memory


class main():
    def __init__(self):
        self.name = "peddireddy"
        self.age = 1000


ca = main()
print(ca.name)