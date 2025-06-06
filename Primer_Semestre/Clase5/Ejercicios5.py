# Creame un diccionario
persona={
    "nombre" : "Maria",
    "edad" : 39,
    "registrado" : True
}
print(persona)

# Accedo a un valor por su clave
print(persona["edad"])

#Anadir una nueva clave-valor
persona["ciudad"] = "Madrid"
persona["Número de hijos"] = 3
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] ="Burgos"
persona["Número de hijos"]= 7
print(persona)

#Eliminar una clave
# del persona["registrado"]
# print(persona)

#Comprobar si una clave ya existe
existe_nombre= "nombre" in persona
print(existe_nombre)

#Comparar dos valores booleanos
es_menor_y_registrado=persona["edad"]<18 and persona["registrado"]
print(es_menor_y_registrado)

#Usar NOT con un booleano
no_veo_registro=not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista con duplicados
numeritos=[7,8,4,7,1,2,3,5,7,2,6,8,4]

#Convierto a conjunto. Porque asi elimino duplicidades
conjuntito=set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos únicos
coleccion_a=set([1,2,2,3])
coleccion_b=set([3,2,1])
mismos_elementitos= coleccion_a==coleccion_b
print(mismos_elementitos)
