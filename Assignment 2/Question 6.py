#Inheritance and method overriding
class Vehicle:
    def start_engine(self):
        print("Vehicle has started")

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started: vroom vroom!")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started: ignition sound!")

vehicles = [Vehicle(), Car(), Bike()]

for v in vehicles:
    v.start_engine()