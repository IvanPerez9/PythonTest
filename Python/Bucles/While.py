'''
Created on 20 jul. 2018

@author: ivan1
'''

import math

i=1

while i<=10 :
    print("Esta vez es la " + str(i))
    i = i+1;

################################
edad = int(input("Introduce la edad: "))

while edad <0 or edad>100 :
    print("Edad negativa, vuelve a introducirla")
    edad = int(input("Introduce la edad: "))

print("Gracias, tu edad es: " + str(edad))

############### Raiz cuadrada

print("Programa de calculo")
numero = int(input("Introduce un numero: "))
intentos = 0;

while numero<0 :
    print("No se puede hallar la raiz de un numero negativo")
    if (intentos == 2):
        print("Demasiados intentos")
        break;
    
    numero = int(input("Introduce un numero: "))
    if (numero < 0):
        intentos = intentos + 1;
        
if intentos < 2 :
    solucion = math.sqrt(numero)
    print("La raiz cuadrad de " + str(numero) + "es " + str(solucion))
        
