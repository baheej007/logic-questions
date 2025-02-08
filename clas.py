class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"

class ElectricCar(Car):  # Inheriting from Car
    def __init__(self, brand, model, price, battery_capacity):
        super().__init__(brand, model, price)  # Calling the parent constructor
        self.battery_capacity = battery_capacity

    def display_info(self):
        return super().display_info() + f", Battery: {self.battery_capacity} kWh"

# Creating objects
car1 = Car("Toyota", "Corolla", 25000)
car2 = ElectricCar("Tesla", "Model S", 80000, 100)

print(car1.display_info())  
print(car2.display_info())