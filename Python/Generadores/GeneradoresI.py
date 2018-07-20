'''
Created on 20 jul. 2018

@author: ivan1
'''

#Generador: Estructuras que estraen valores de una funcion y los almacenan en objetos iterables
#Cada vez quie pides un valor , se queda en pausa el generador
#En lugar de Return hay un Yield, construye un objeto iterable con lo que se pide, se devuelven de 1 en 1 
#mas eficiente, cuando buscamos solo 1 elemento en concreto 

def numeroPares (limite):
    numero = 1;
    miLista = [];
    while numero < limite :
        miLista.append(numero*2);
        numero += 1;
    return miLista

print(numeroPares(10))

#Con Generadores ahora:

def numeroParesG (limite):
    numero = 1;
    while numero < limite :
        yield numero*2
        numero += 1;
        
devuelvePares = numeroParesG(10);
#for i in devuelvePares:
#   print(i)
    
#De 1 en 1 , con un generador no necesitas toda la lista, es la eficiencia 
print(next(devuelvePares))
print(next(devuelvePares))
