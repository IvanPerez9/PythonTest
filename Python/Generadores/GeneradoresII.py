'''
Created on 20 jul. 2018

@author: ivan1
'''

#Intruccion Yield From 
#Simplifica el codigo de los generadores en caso de utilizar bucles anidados 

def DevolverCiudades (*ciudades): #Con * numero indeterminado de elementos y con tupla
    for elemento in ciudades:
        yield from elemento #Coge el subelemento 

ciudadesDevueltas = DevolverCiudades("Madrid" , "BCN" , "Bilbao" , "Valencia")

print(next(ciudadesDevueltas))

