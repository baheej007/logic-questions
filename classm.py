class Car:
    total_cars = 0  # Class variable

    def __init__(self, model):
        self.model = model
        Car.total_cars += 1

    @classmethod
    def show_total_cars(cls):
        return f"Total cars in showroom: {cls.total_cars}"

# Creating car objects
car1 = Car("Toyota")
car2 = Car("Honda")

print(Car.show_total_cars())  # Output: Total cars in showroom: 2
