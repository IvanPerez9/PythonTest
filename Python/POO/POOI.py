'''
Created on 24 jul. 2018

@author: ivan1
'''


# Primeros dos videos son teoricos

class Coche ():
    
    largoChasis = 250;
    anchoChasis = 120;
    ruedas = 4;
    enmarcha= False;
    
    #Comportamiento == Metodos
    # This es Self , obligado a ponerlo
    
    def arrancar(self):
        self.enmarcha = True;
        
    def estado (self):
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    
miCoche=Coche()
print(miCoche.largoChasis);
miCoche.arrancar()
print(miCoche.estado());