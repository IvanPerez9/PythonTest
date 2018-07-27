'''
Created on 27 jul. 2018

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
        

class Furgoneta(Vehiculos):
    
    def carga (self,cargar):
        self.cargado = cargar;
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "No esta cargada"

class Moto (Vehiculos): #Asi hereda 
    hcaballito ="";
    
    def caballito (self):
        self.hcaballito = "Voy haciendo el caballito"
    
    def estado(self):
        Vehiculos.estado(self) # Se hereda con todo a la vez, copiar y pegar , ¿  No super ? 

class Velectricos ():
    def __init__ (self):
        self.autonomia = 100;
        
    def cargarEnergia (self):
        self.cargando = True;

miMoto = Moto("Honda", "CBR")
miMoto.caballito();
miMoto.estado()

miFurgoneta = Furgoneta("Renault" , "Kangoo")
miFurgoneta.arrancar();
miFurgoneta.estado();
print(miFurgoneta.carga(True))

class BicicletaE (Vehiculos, Velectricos): #Hereda de 2 , se da preferencia al primero
    
    pass; 

miBici = BicicletaE();

