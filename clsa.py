class Car:
    def move(self):
        print("Drive!")

class Boat:
    def move(self):
        print("Sail!")

class Plane:
    def move(self):
        print("Fly!")

vehicles = [Car(), Boat(), Plane()]
for vehicle in vehicles:
    vehicle.move()
