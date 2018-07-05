'''
Created on 5 jul. 2018

@author: ivan1
'''

#Parecidas a las listas, pero inmutables. No se anaden ni se borran etc 
#Sirven para ocupar menos espacio y ser mas rapidas

#Se usan como claves de un diccionario (listas no) 

#Son iguales pero con parentesis

nombreTupla = ("Juan"  , 13, 145);
print(nombreTupla[2]);

#Metodos de conversion de tupla a lista

miLista = list(nombreTupla);
print(miLista)

miTupla = tuple(miLista)
print(miTupla)

#Comprobar elementos igual

print("Juan" in nombreTupla)
print(nombreTupla.count(13)) # Cuantos elementos de ese tipo 

print(len(miTupla)); #Distancia

#Desempaquetado de tupla

miTupla2 = ("juan" , 13, 3465, 7.6);
nombre,dia,mes,decimal = miTupla2;  #Asigna por orden a la tupla

print(nombre);
print(decimal);




