# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:13:21 2020

@author: PC
"""

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_reading = 0
        self.oil_reading= 0
        
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make + ' '+self.model
        return long_name.title()
    def read_odometer(sefl):
        print("This car has " + str(sefl.odometer_reading) + " miles on it")
        
    def read_fuel(sefl):
        print ("This car has " + str(sefl.fuel_reading) + " litters of gasoline on it")
        
    def read_oil(sefl):
        print ("This car has " + str(sefl.oil_reading) + " porcentage of oil level")
my_new_car = Car('audi','a4',2020)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()
my_new_car.fuel_reading=20
my_new_car.read_fuel()
my_new_car.oil_reading=70
my_new_car.read_oil()