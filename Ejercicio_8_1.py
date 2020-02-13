# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:37:45 2020

@author: PC
"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    def charge(self):
        print("The car is charging ....")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def charge(self):
        print("The battery is almost empty, the car is charging")
my_tesla = ElectricCar('tesla','model s',2020)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.charge()

class HybridCar (Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.gasoline_level = 90
        self.battery_size = 70
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def describe_gasoline(self):
        print("This car has " + str(self.gasoline_level) + " porcentage of gasoline level")
    def charge(self):
        print("The battery is almost empty, the car is charging")
my_ford_fussion =  HybridCar('Ford','Fussion',2019)
print(my_ford_fussion.get_descriptive_name())
my_ford_fussion.describe_battery()
my_ford_fussion.describe_gasoline()
my_ford_fussion.charge()

class FuelCar (Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.gasoline_level = 80
    def describe_gasoline(self):
        print("This car has " + str(self.gasoline_level) + " porcentage of gasoline level")
    def charge(self):
        print("The battery is almost empty, the car is charging")
my_lambo =  FuelCar('Lamborghini','Reventon',2009)
print(my_lambo.get_descriptive_name())
my_lambo.describe_gasoline()
my_lambo.charge()