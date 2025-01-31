class Grandparent:
    def feature1(self):
        print("Feature from Grandparent")

class Parent(Grandparent):
    def feature2(self):
        print("Feature from Parent")

class Child(Parent):  # Inherits from Parent (which inherits from Grandparent)
    def feature3(self):
        print("Feature from Child")

c = Child()
c.feature1()
c.feature2()
c.feature3()
