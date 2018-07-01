'''
Created on 1 jul. 2018

@author: ivan1
'''

# Tipos, operadores y variables

# Exponente en python **
5**2
valor = 5**2 ;
print(valor);

# El tipo de la variable es dependiendo del contenido 
# Todo es un objeto

nombre = 5 
type(nombre);
#En la consola sale el tipo de datos con type

#Condicionales
numero1= 5;
numero2= 7
if numero1 > numero2:
    print("El numero 1 es mayor al 2");
else:
    print("El numero 2 es mayor")  ;
      
   
#Funciones en python 
# Pueden devolver valores y tener parametros/argumentos

def funcion1 ():
    print("Hola repetir funcion");
    
contador=4;
for i in range(4):
    funcion1();    

########## SIEMPRE PASA LOS PARAMETROS POR REFERENCIA

def suma (num1, num2):
    print(num1+ num2);
    resultado = num1 + num2
    return resultado;

suma(5, 7);
print(suma(5, 7))
suma(2, 3);
suma(45436, 534453);

    