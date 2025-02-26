"""
 -A creational design pattern that provides an interface to create objects
  without specifying their exact class.
 -needs anujiye obj make kora

"""
class Car:
    def driver(self):
        return "Driving a car"
        


class Bike:
    def driver(self):
        return "Riding a bike"
        


class VehicleFactory:
    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        else:
            return ValueError("Unknown vehcile!")


vehicle = VehicleFactory.get_vehicle("car")
print(vehicle.driver())
#Driving a car



vehicle = VehicleFactory.get_vehicle("bike")
print(vehicle.driver())