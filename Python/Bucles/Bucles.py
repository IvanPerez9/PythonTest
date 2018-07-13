'''
Created on 12 jul. 2018

@author: ivan1
'''

#Tipos determinados (numero determinado de veces) e indeterminados (No se sabe a priori) 

# Se parece a un for-each 

for i in [1,2,3]:
    print("Hola")

for i in ["primavera", "verano", "Otono", "invierno"]:
    print("Hola")

for i in ["primavera", "verano", "Otono", "invierno"]:
    print(i)

# Bucles II 

for i in ["primavera", "verano", "Otono", "invierno"]:
    print(i , end="")

email = False;
for i in "ivan120695@gmail.com":
    if (i == "@"):
        email=True

if email == True:
    print("Email correcto")
else:
    print("Email incorrecto")
    
##############

contador=0;
email = False;
nick = input("Introduce tu email: ")
for i in nick:
    if (i == "@" or i=="."):
        contador= contador + 1; # Debe valer 2 para que este bien

if contador == 2:
    print("Email correcto")
else:
    print("Email incorrecto")
    
    
    