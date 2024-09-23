class A:
    def __init__(self):
        print("parent constructor")
    def find_area(self, a=None,b=None): #method overriding
        if a!=None and b!=None:
            print("Area of rect:", a*b)
        elif a!=None:
            print("area of square", a**2)
        else:
            print("Nothing to find")
    def showData(self):
        print("i am in A")

class B(A):
    def __init__(self):
        super().__init__() #calling parent constructor
        print("child constructor")
    def showData(self): #method overloaded in child class
        print("I am in B")
    def addNums(a,b):
        return a + b

    @classmethod #used to bound method to class rather than an instance of it
    def setNum(self, a):
        self.a = a
B.addNums = staticmethod(B.addNums) #makes a method  static

obj = A()
obj.find_area()
obj.find_area(2)
obj.find_area(3,2)
obj.showData()
obj = B()
obj.showData()
print(B.addNums(4,5))
B.setNum(3)
print(obj.a)
