Abstraction in Python

Abstraction hides implementation details and only exposes essential features.


---

Example: Using Abstract Class

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


---

Explanation:

1. ABC (Abstract Base Class) → Prevents object creation.


2. @abstractmethod → Forces subclasses to implement make_sound().


3. Subclasses (Dog, Cat) → Provide their own implementation.



Abstraction ensures only the necessary details are exposed while hiding the implementation!

