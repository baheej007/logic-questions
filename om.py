class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overriding parent method
        print("Dog barks")

a = Animal()
a.sound()

d = Dog()
d.sound()  # Calls overridden method
