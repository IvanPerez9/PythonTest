'''
Created on 23 jul. 2018

@author: ivan1
'''
import math
#Excepciones propias con Raise , cuando lleguemos a POO 

def evaluaEdad (edad):
    
    #Hay que definir una clase si quieres "MiError" 
    
    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres viejo"
    elif edad < 100:
        return "Cuidate"

print(evaluaEdad(-45))

def Raiz(num1):
    
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1 = (int(input("Introduce el numero: ")))

try:
    print(Raiz(op1))
except ValueError as ErrorNumNegativo: #Le doy un alias 
    print(ErrorNumNegativo)

print("Todo bien")

