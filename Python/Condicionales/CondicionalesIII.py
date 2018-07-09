'''
Created on 9 jul. 2018

@author: ivan1
'''

#No tiene Switch , se pueden usar diccionarios, o concatenar operadores de comparacion


edad = 7

def evaluacionEdad (edad):
    if 0 < edad < 100 :
        print("Es correcta")
    else :
        print("Edad incorrecta")

# Esto hace lo mismo que el condicionales II pero con distinta sintaxis 

salarioPresidente= int(input("Introduce salario "))
print("Salario : " + str(salarioPresidente)) #Usar funcion str no vale solo con el +

#Fuertemente tipado

salarioDirector= int(input("Introduce salario "))
print("Salario : " + str(salarioDirector))
salarioJefeArea= int(input("Introduce salario "))
print("Salario : " + str(salarioJefeArea))
salarioAdmin= int(input("Introduce salario "))
print("Salario : " + str(salarioAdmin))

if salarioAdmin < salarioJefeArea < salarioDirector < salarioPresidente:
    print("Bien")
else:
    print("Falla")

