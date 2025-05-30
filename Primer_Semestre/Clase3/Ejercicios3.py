import math
import random

#Ejercicio 1
#nombre = input("Dime tu nombre y apellido: ")
#print(nombre)
#nombre_usuario = nombre.lower()
#print(nombre_usuario)
#numero_aleatorio = random.randint(1,50)
#print(numero_aleatorio)
#print(nombre_usuario, numero_aleatorio)

#Ejercicio 2

#frase =input("Dime una frase: ")
#num_caracteres = len(frase)
#print(num_caracteres)
#print("Python" in frase)
#print(frase.upper())
#print(frase[-31:], "y", frase[:19])

#Ejercicio 3

#precio_producto = float (input ("Dime un precio: "))
#descuento = precio_producto*0.15
#precio_final = precio_producto - descuento
#print(f"Precio con descuento: ${precio_final:.2f}")
#print(f"Redondeado hacia arriba: ${math.ceil(precio_final)}")

#Ejercicio 4

#nombre_producto = input("Dime el nombre de un producto: ")
#precio = input ("Dime su precio: ")
#print(nombre_producto.upper())
#precio_numero= int(precio)
#print("Precio con dos decimales: {:.2f}".format(precio_numero))
#print("Dime el código ASCII de la primera letra del producto: ", ord(nombre_producto[:1]))

#Ejercicio 5

#lista = input("Dime números separadas por coma: ")
#enteros = list(set(map(int, lista.split(","))))
#print("Lista en orden y sin duplicados: ", sorted(enteros))

#Ejercicio 6

#dime_nombre = input("Dime tu nombre: ")
#dime_edad = int (input("Dime tu edad "))
#dime_ciudad = input("y dime en que ciudad vives: ")
#if dime_edad<=18:
   #print(f"Mi nombre es {dime_nombre}, tengo {math.ceil(18)} y vivo en {dime_ciudad}")
#else:
 #print(f"Mi nombre es {dime_nombre}, tengo {dime_edad} y vivo en {dime_ciudad}")

#Ejercicio 7

# nombre = input("Dime tu nombre: ")
# numero = random.randint(1,50)
# contrasena =f"Tu contraseña nueva es: {nombre[:1].upper()}{numero}{"*"}"
# print(contrasena)

# Ejercicio 8

# nombre = input("Dime tu nombre: ")
# lista = ["Pablo", "Juan", "Matias", "Penélope", "Maria", "Florencia"]
# verificar = nombre in lista
# print(verificar)

# Ejercicio 9

# nombre= input("Dime tu nombre: ")
# apellido = input("Dime tu apellido: ")
# cambio_nombre = nombre.lower()
# cambio_apellido = apellido.upper()
# alias = cambio_nombre[:3] + cambio_apellido[:3]
# print(alias)

# Ejercicio 10

# # frase= float (input("Dime un número decimal: "))
# resultado = round(frase,2)
# print(resultado)
# print(resultado**2)
# print(resultado**0.5)