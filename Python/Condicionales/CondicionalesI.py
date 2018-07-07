'''
Created on 7 jul. 2018

@author: ivan1
'''

#IF
#Funcion

def evaluacion(nota):
    valoracion="Aprobado"
    if nota<5: 
        valoracion= "Suspenso"
    return valoracion;


print("Programa de evaluacion")
nota_alumno=input("Introduce la nota: "); #Cualquier cosa por input es string ... Funcion int() como casteo

print(evaluacion(int(nota_alumno)))     #funcion int
