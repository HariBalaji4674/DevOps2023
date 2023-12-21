print("Hello World")

class a:
    def inti(self):
        print("Hello Mr. Peddireddy")
class b :
    def inti2(self):
        print("Hello Mrs Hari Vardhan")

class b(a):
    def namma(self):
        print("Hello World")
        pass

m1 = b()
m1.inti()
m1.namma()

class human:
    def myHu(self,name=None):
        if name is not None:
            print("Hello ",name)
        else:
            print("Hello")
h = human()
h.myHu()

