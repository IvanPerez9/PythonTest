'''
Created on 25 jul. 2018

@author: ivan1
'''

class Vehiculos():
    
    def __init__ (self,marca,modelo):
        self.marca = marca;
        self.modelo = modelo;
        self.enmarcha = False;
        self.acelera = False;
        self.frena = False;
    
    def arrancar (self):
        
        self.enmarcha = True;
        
    def acelerar (self):
        
        self.acelera = True;
        
    def frenar (self):
        
        self.frena = True;
        
    def estado (self):
        
        print("Marca: " , self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha)
        

class Moto (Vehiculos): #Asi hereda 
    pass

miMoto = Moto("Honda", "CBR")
miMoto.estado()