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
        self.__enmarcha= False;
    
    #Comportamiento == Metodos
    # This es Self , obligado a ponerlo
    
    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos;
        if (self.__enmarcha == True):
            chequeo = self.__checkeo_interno()
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"
        
    def estado (self):
        print("El coche tiene " , self.__ruedas , "ruedas")
        print("El coche tiene " , self.__anchoChasis , "cm de ancho")
        print("El coche tiene " , self.__largoChasis , "cm de largo")

      
    #Encapsular el metodo igual __ 
      
    def __checkeo_interno (self):
        print("Realizando chekeo interno")
        self.gasolina = "ok";
        self.puerta = "cerradas"
        self.aceite = "ok" 
        
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puerta =="cerradas"):
            return True;
        else:
            return False;



miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("Acontinuacion creamos el segundo objeto")

miCoche2 = Coche();
print(miCoche2.arrancar(False))
miCoche2.estado()
