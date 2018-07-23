'''
Created on 23 jul. 2018

@author: ivan1
'''

#Puedo usar varios except seguidos 
#Finally hace que ese codigo se ejecuta siempre 
# Try siempre con except o finally 

from builtins import str

def divide ():
    
    try:
    
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        
        print("La division es: " + str(op1/op2))
        
    except ValueError:
        
        print("El valor introducido es erroneo")
        
    except ZeroDivisionError:
        
        print("No puedes dividir entre 0")
        
    finally:
    
        print("Calculo finalizado");

divide()