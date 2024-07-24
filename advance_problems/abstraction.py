# Abstraction
# Abstraction involves hiding complex implementation details and showing only the essential features of the object.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

    def drive(self):
        print("Car is being driven")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")

    def stop_engine(self):
        print("Bike engine stopped")

    def drive(self):
        print("Bike is being ridden")

def test_vehicle(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.drive()
    vehicle.stop_engine()

# Using the test_vehicle function to demonstrate abstraction
car = Car()
bike = Bike()

test_vehicle(car)
test_vehicle(bike)
