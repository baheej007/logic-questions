class A:
    def showA(self):
        print("Inside A")

class B(A):
    def showB(self):
        print("Inside B")

class C(B):
    def showC(self):
        print("Inside C")

obj = C()
obj.showA()  # A → B → C
obj.showB()
obj.showC()
