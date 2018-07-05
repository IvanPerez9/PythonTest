'''
Created on 5 jul. 2018

@author: ivan1
'''


#Los diccionarios: Como listas pero con clave:valor (HashTable de java) 

midiccionario={"Alemania" : "Berlin" , "Francia": "Paris" , "Reino Unido" : "Londres" , "Espana": "Mardrid"}
print(midiccionario["Francia"])

midiccionario["Italia"] = "Lisboa"
midiccionario["Italia"] = "Roma"
print(midiccionario);

del midiccionario["Reino Unido"] #Borra
print(midiccionario.keys())
print(midiccionario.values())
print(len(midiccionario))

###################################################

midiccionario2={"Alemania" : "Berlin" , 23: "Jordan" }

miTupla=["Espana", "Francia", "Alemania"]
midiccionario={miTupla[0]:"Madrid"}
print(midiccionario)


#Puedes meter dentro tuplas, o diccionarios dentro de diccionarios