class myClass:
    def __init__(self):
        print("Hari Vardhan reddy")
m1 = myClass()

class myClass1:
    def __init__(self,a,b):
        print(a,b)
m2 = myClass1(10,20)

i = 10
j = 20
class myClass2:
    k = "kullu"
    j = "jullu"
    def __init__(self,a,b):
        print(a,b)
        print(i,j)
        print(self.j,self.k)

m1 = myClass2(50,60)

carName1 = "BMW"
carName2 = "Ferrari"
carName3 = "Lamborghini"

class cars:
    carName4 = "Bullet"
    carName5 = "Harrier"
    carName6  = "Fortuner"
    def carNames(self):
        print("Global Varibales" , carName3,carName1,carName2)
    def carNames1(self):
        print("Class Level Variables", self.carName4,self.carName5,self.carName6)
    def carNames2(self,carName7,carName8,carName9):
        print("Local Variables",carName7,carName8,carName9)

mc = cars()   
mc.carNames()
mc.carNames1()
mc.carNames2("bullet","kgf","manohara")

# Inside the Class and Inside the Function with same variables 
# To Call these variables
# To Call Local Variables --> Directly we can call
# To Call Global Variables 
# print(globals()[variable1],globals()[variable2])
# to call class variables
# print(self.variable1,self.varaible2)



