from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def make_sound(self):  # Abstract method
        pass

class Dog(Animal):  
    def make_sound(self):  
        print("Dog barks")  # Implementation

class Cat(Animal):  
    def make_sound(self):  
        print("Cat meows")  # Implementation

d = Dog()
d.make_sound()  # Output: Dog barks

c = Cat()
c.make_sound()  # Output: Cat meows