'''
Created on 24 jul. 2018

@author: ivan1
'''


# Primeros dos videos son teoricos

class Coche ():
    
    #Constructor
    #Encapsular una propiedad, proteger para no ser modificada desde fuera. Por ejemplo ruedas Video 27 18 min
    #Ojo a esto, accesible desde dentro no desde fuera
    
    def __init__ (self):
        self.__largoChasis = 250;
        self.__anchoChasis = 120;
        self.__ruedas = 4;  #Desde fuera de la clase no se puede modificar 
        self.enmarcha= False;
    
    #Comportamiento == Metodos
    # This es Self , obligado a ponerlo
    
    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos;
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
    def estado (self):
        print("El coche tiene " , self.__ruedas , "ruedas")
        print("El coche tiene " , self.__anchoChasis , "cm de ancho")
        print("El coche tiene " , self.__largoChasis , "cm de largo")

miCoche=Coche()
print(miCoche.largoChasis);
print(miCoche.arrancar(True))
miCoche.estado()

print("Acontinuacion creamos el segundo objeto")

miCoche2 = Coche();
print(miCoche2.arrancar(False))
miCoche2.ruedas = 2; #Variables de __ y sin son variables distintas
miCoche2.estado()
