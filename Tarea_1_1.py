# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:45:50 2020

@author: PC
"""

class Restaurant ():
    def __init__ (self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print ("El nombre del restaurante es " + self.restaurant_name.title())
        print ("El tipo de comida es " + self.cuisine_type.title())
    def open_restaurant(self):
        print ("El restaurante es " + str('abierto'))
        
    def read_served(sefl):
        print("El numero de clientes atendidos es: " + str(sefl.number_served))
    
    def set_number_served(self,number):
        if number>=self.number_served:
            self.number_served=number
        else:
            print ("El número debe ser mayor")
            
my_restaurant = Restaurant ('Salads life','comida vegana')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.read_served()
my_restaurant.number_served=9
my_restaurant.read_served()
my_restaurant.set_number_served(20)
my_restaurant.read_served()
my_restaurant.set_number_served(10)