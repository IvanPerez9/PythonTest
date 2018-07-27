'''
Created on 27 jul. 2018

@author: ivan1
'''

class coche ():
    
    def desplazamiento (self):
        print("Me desplazo usando 4 ruedas")
        
class Moto():
    
    def desplazamiento (self):
        print("Me desplazo con 2 ruedas")
        
class Camion ():
    
    def desplazamiento (self):
        print("Uso 6 ruedas ")
        

def desplazamientoVehiculo (vehiculo): #Identifica cual es y llama al desplazamiento que es 
    vehiculo.desplazamiento()
    
miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)