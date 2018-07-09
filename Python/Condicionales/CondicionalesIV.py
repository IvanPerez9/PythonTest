'''
Created on 9 jul. 2018

@author: ivan1
'''
import sys

#Operadores logicos and y or . Es case sensitive 

#Tambien operador IN 

#Alumno con beca o sin 

distancia = int (input("Introduce la distancia a la escuela "))
print(distancia)

hermanos = int (input("Introduce numero de hermanos "))
print(hermanos)

salario = int (input("Introduce salario bruto "))
print(salario)

if distancia>40 and hermanos>2 and salario<=20000 :
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")

########################################

def operadorIN():
    print("Asignaturas optativas")
    print("Son: Informativa grafica - Pruebas de SW - Usabilidad y Accesibilidad")
    
    asignatura = input("Escribe la asinatura escogida: ")
    
    if asignatura in ("Informatica grafica" , "Pruebas de SW" , "Usabilidad y accesibilidad"):
        #Si no es de tipo string sin "" 
        print("Asignatura elegiga: "  + asignatura)
        return asignatura
    else:
        return print("No esta esa asignatura")
    
    sys.exit(0)

print(operadorIN())