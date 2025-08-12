import math
#Funciones

#Ejerciio 1: Calcular el área de un círculo

# def calcular_area (radio):
#     area = math.pi * radio**2
#     return area
# radio = int(input("Introduce el radio: \n"))
# print(f"El área de un círculo de radio {radio} es {calcular_area(radio):.2f}")

#Ejercicio 2: Configura un mensaje de bienvenida

# def datos (nombre, apellido, edad):
#     print(f"Bienvenid@ {nombre} {apellido}, tienes {edad} años")
#
# nombre = input("Introduce tu nombre: ")
# apellido = input("Introduce tu apellido: ")
# edad = input("Introduce tu edad: ")
#
# datos(nombre,apellido,edad)

#Ejercicio 3: Calcular el factorial de un número

# def calculo_factorial(numero):
#     resultado = 1
#     for i in range (numero,1,-1):
#         resultado *= i
#     return resultado
#
# numero = int (input("Introduce un número entero positivo: "))
# print(calculo_factorial(numero)

#Ejercicio 4: Verificar si un número es primo

# def numero_primo (numero):
#     '''un número es primo si solo es divisible entre 1 y si mismo'''
#     for i in range(2, numero):
#         if numero%i == 0:
#             return False
#     return True
# numero = int(input("Dime un numero entero: "))
# print(numero_primo(numero))

#Ejercicio 5: Calcular la suma de dígitos de un número

# def sumatoria (numero):
#     resultado = 0
#     while numero > 0:
#        resultado += numero%10
#        numero//=10
#     return resultado
#
# numero = int(input("Introduce un número entero: "))
# print(f"La suma de los dígitos del número {numero} es: {sumatoria(numero)}")

#Ejercicio 6: Encontrar el máximo y el mínimo de una lista

# Ejercicio 7: Incrementar cada elemento de una lista

# def incrementa_lista (lista, numero):
#     for i in range (len(lista)):
#         lista[i] += numero
#     return lista
#
# numeros = input("Introduce una lista de numeros separadas por coma: ").split(",")
# lista = [int(num)for num in numeros]
# numero = int(input("Introduce el incremento: "))
# print(incrementa_lista(lista,numero))