'''
Created on 20 jul. 2018

@author: ivan1
'''
## CONTINUE PASS Y ELSE para FOR y WHILE Video 18 
 
#pass devuelve null
#continue pasa a la siguiente, crear clases nulas y eso
#else como en un if 

for letra in "Python" :
    
    if letra == "h": #Ignora la linea de la H 
        continue
    
    print("viendo la letra: " + str(letra))
    
    
########################################## else para for

email = input("Introduce tu email, por favor: ")

for i in email :
    if i=="@":
        arroba = True;
        break;
else :
    arroba=False;

print(arroba)