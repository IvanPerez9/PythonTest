'''
Created on 4 jul. 2018

@author: ivan1
'''


# Listas - equivalente a Array , puede guardar diferentes tipos, y se puede expandir dinamicamente
# OJO CON LAS DIFERENCIAS, DINAMICO Y DISTINTOS TIPOS

#nombreLista=[elem1, elem2]

miLista = ["Ivan", "Maria", "Pepe"] ;

print(miLista[:]); #Toda la lista
print(miLista[0]);
print(miLista[-3]); #Va al reves

#Porcion de Lista

print(miLista[0:2]); #de 0 a 2 
print(miLista[:2]); 
print(miLista[2:]); 

#Anadir

miLista.append("Hola");
print(miLista[:]);
print(miLista);

miLista.insert(2, "En el 2");
print(miLista);

#anadir a la lista otra
miLista.extend(["Otra", "Lista", "Jaja"])
print(miLista)

print(miLista.index("Ivan")) #Devuelve el indice , del primer elemento

#Si esta en lista, boolena

print("Maria" in miLista)

miLista = [8, "Maria", 7.9] ; #Distintos tipo
print(miLista[2])

#Eliminar

miLista.remove(8)
print(miLista)

#Eliminar el ultimo elemento de la lista
miLista.pop();
print(miLista);

#Sumar listas
miLista2 = ["Ivan", "Maria", "Pepeeee", "Hola"] ;
miLista3 = miLista + miLista2;

print(miLista3)


