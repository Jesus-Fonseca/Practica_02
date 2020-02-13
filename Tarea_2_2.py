# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:19:24 2020

@author: PC
"""

class User():
    def __init__(self,first,second):
        self.first_name = first
        self.second_name = second
        self.num_intentos = 0
    def describe_user (self):
        print ("Primer apellido: " + self.first_name.title())
        print ("Segundo apellido: " + self.second_name.title())
    def greet_user (self):
        print ("Bienvenido " + self.first_name.title() + " " + self.second_name.title())
        
    def read_intentos(sefl):
        print("El número de intentos es: " + str(sefl.num_intentos))
        
    def increment_login_attempts(self,intentos):
        self.num_intentos = intentos
        intentos += 1
        
    def reset_login_attempts(self,intentos):
        self.num_intentos = intentos
        intentos == 0
    
    def secure_account(self,intentos):
        if intentos<=10 :
            self.num_intentos = intentos
        else:
            print ("Ha excedido el nùmero de intentos permitidos")

usuario = User ('Lopez','Valencia')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Beltran','Guzman')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Sanchez','Rodriguez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Perez','Dominguez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Flores','Aguilar')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Zenil','Perez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Neri','Garcia')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Acosta','Alcoser')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Prado','Hernandez')
usuario.describe_user()
usuario.greet_user()
usuario = User ('Morua','Alvarez')
usuario.describe_user()
usuario.greet_user()

usuario.num_intentos=2
usuario.read_intentos()
usuario.increment_login_attempts(1)
usuario.read_intentos()
usuario.reset_login_attempts(2)
usuario.read_intentos()
usuario.secure_account(11)
usuario.read_intentos()