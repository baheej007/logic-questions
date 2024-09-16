class Car:
  def __init__(self, model, color): 
    self.model = model 
    self.color = color
  def display_info(self): 
    print(f" Model: {self.model}, Color: {self.color} ")
car1=Car("Toyota", "Red") 
car1.display_info()
