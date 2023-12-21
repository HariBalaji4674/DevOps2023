'''
Class Inside the Class

Object Should be created inside the class

'''

class Student:
    def __init__(self,name,age,section,):
        self.name = name
        self.age = age
        self.section = section
        self.lap = self.marks()
    def show(self):
        print(self.name, self.age, self.section)

    class marks:
        def __init__(self):
            self.maths = 80
            self.science = 90
            self.social = 100
        def show(self):
            print(self.maths, self.science, self.social)


std1 = Student("Naveen",25,23)
std2 = Student("Hari",23,2090)

std1.show()

st3 = Student.marks()
st3.show()

