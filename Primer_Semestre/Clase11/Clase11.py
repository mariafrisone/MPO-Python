#Diccionarios (hashmap en java)

#Ejercicio 1: Capitales y países

#1 variables
#2 bucle que lee y registra las entradas del pais-capital
#3 pedir un pais y mirar si existe en el diccionario

# paises = {}
# entrada = input("Indica un valor dela forma 'Pais-Capital' o escribe FIN INSERCIONES para finalizar: \n")
#
# while entrada != "FIN INSERCIONES".lower():
#     #["España" - "Madrid"]
#     pais = entrada.split("-")[0].lower()
#     capital = entrada.split("-")[1].lower()
#     paises [pais] = capital
#     entrada = input("Indica un valor dela forma 'Pais-Capital' o escribe FIN INSERCIONES para finalizar\n")
#
# pais_usuario=input("Introduce el nombre del país que quiere consultar: ").lower()
# if pais_usuario in paises:
#     print(f"La capital de {pais_usuario} es {paises[pais_usuario]}")
# else:
#     print("No existe ese registro en el diccionario")

#Ejercicio 2: Contar palabras en un texto
'''
1 Definir variables
2 Bucle que recorra las palabras y mire si:
    2.1 Si ya existian: sumo 1 a la frecuencia anterior
    2.2 Creo una entrada en el diccionario con frecuencia 1
3 Imprimir diccionario

palabras={}
texto=input("Introduce una frase\n").lower().split()

for palabra in texto:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1
print(palabras)
'''
from platform import machine

#Ejercicio 3: Inventario de productos
#
# inventario = {}
# opcion = -1
#
# while opcion != 4:
#     print("Escoge una opción: ")
#     print("1. Añadir producto")
#     print("2. Eliminar producto")
#     print("3. Consultar producto")
#     print("4. Salir")
#     opcion=int(input("Introduce una opción: "))
#
#     if opcion == 1:
#         nombre = input("Introduce un producto: ")
#         cantidad = input("Introduce una cantidad: ")
#         inventario[nombre] = cantidad
#     elif opcion == 2:
#         nombre = input("Introduce el producto a eliminar: ")
#         if nombre in inventario:
#             del inventario[nombre]
#             print(f"Producto {nombre} eliminado del inventario")
#         else:
#             print(f"No existe el producto {nombre} en el inventario")
#     elif opcion == 3:
#         nombre = input("Introduce producto a consultar: ")
#         if nombre in inventario:
#             print(f"El producto {nombre} tiene una cantidad {inventario[nombre]} unidades")
#         else:
#             print(f"No existe el producto {nombre} en el inventario")
#     elif opcion > 4 or opcion < 1:
#         print(f"La opción {opcion} no existe en la lista de comandos")
# print("Saliendo")

# Ejercicio 4: Tupla de números

# numeros = input("Dime lista de números enteros: ").split(",")
# numeros =[int (num) for num in numeros]
# tupla=tuple(numeros)
#
# suma=0
# promedio=0
# maximo=float('-inf')
# minimo=float('inf')
#
# for numero in tupla:
#    suma += numero
#    if numero > maximo:
#     maximo = numero
#     if numero < minimo:
#         minimo = numero
#
# promedio = suma / len (tupla)
#
# print(f"Suma: {suma}")
# print(f"Promedio: {promedio}")
# print(f"Maximo: {maximo}")
# print(f"Minimo: {minimo}")


#Ejercicio 5: Biblioteca digital

