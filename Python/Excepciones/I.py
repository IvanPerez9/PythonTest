'''
Created on 23 jul. 2018

@author: ivan1 video 21
'''

# Es un error en tiempo de ejecucion
# Con el codigo de error, te da lo que necesitas para capturar la excepcion
# Try y except (nombre del error) 

def suma (num1,num2):
    return num1+num2;

def resta (num1, num2):
    return num1-num2;

def multiplica (num1, num2):
    return num1*num2;

def divide (num1,num2):
    try:
        return num1/num2;
    except ZeroDivisionError:
        print("No se puede divir entre cero")
        return "Operacion erronea"

#Bucle infinito
while True:
    try:
        op1 = (int(input("Introduce el primer operando: ")))
        op2 = (int(input("Introduce el segundo operando: ")))
        break;
    except ValueError:
        print("Los valores introducidos no son correctos, intentalo de nuevo ")

operacion = input("Que operacion deseas realizar (suma, resta, multiplica, divide): ")

if operacion == "suma":
    print(suma(op1, op2))
elif operacion == "resta":
    print(resta(op1, op2))
elif operacion == "multiplica":
    print(multiplica(op1, op2))
elif operacion == "divide":
    print(divide(op1, op2))
else:
    print("Operacion no contemplada");
    
print("Operacion ejecutada")