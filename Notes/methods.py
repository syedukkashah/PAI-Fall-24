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

obj = A()
obj.find_area()
obj.find_area(2)
obj.find_area(3,2)
obj.showData()
obj = B()
obj.showData()
