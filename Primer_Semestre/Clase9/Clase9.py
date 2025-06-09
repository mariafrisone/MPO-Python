#Estructuras de repeticion: While

#Ejercicio 9: Suma acumulativa

# print("Dime números enteros y cuando acabes introduce 0: ")
# numeros= int(input())
# suma=0
# while numeros !=0:
#     suma+=numeros
#     numeros=int(input())
# print(f"El resultado es {suma}")

# Ejercicio 10: Akinator numérico
# import random
# numero_aleatorio = random.randint(1,100)
# numero_usuario = int(input("Introduce un número del 1 al 100: "))
#
# while numero_usuario != numero_aleatorio:
#     if numero_usuario>numero_aleatorio:
#         print("Lo siento, es demasiado alto")
#     else:
#         print("Lo siento el número es muy bajo")
#     numero_usuario = int(input("Introduce un número del 1 al 100: "))
#
# print("Adivinaste!!!!!")

#Ejercicio 11: Media de notas
#
# num_evaluaciones = int(input("Introduce evaluaciones: "))
# for i in range(num_evaluaciones):
#     notas = float(input("Dime la nota a promediar: "))
#     num_notas = 0
#     media = 0
#     while notas != -1:
#        num_notas += 1
#        media += notas
#        notas = float(input("Dime la nota a promediar: "))
#     print(f"Nota media evaluación {i+1}: {media/num_notas}")

#Ejercicio 12: Mayor y menor

# mayor = float('-inf)
# menor = float('inf')
# numero = int(input("Introduce un valor (0 para terminar): "))
# while numero != 0:
#         if numero > mayor:
#             mayor = numero
#         if numero < menor:
#             menor = numero
#         numero = int (input("Introduce un valor (0 para terminar): "))
#
# print(f"Mayor: {mayor} Menor: {menor}")

#Ejercicio 13: Número de cifras
#
# numero = int (input("Dime un número entero positivo (-1 para acabar): "))
#
# while numero != -1:
#     cifras = 1
#     copia_num = numero
#     while numero > 9:
#         cifras += 1
#         numero//= 10
#     print(f"El número de dígitos de {copia_num} es {cifras}")
#     numero = int(input("Dime un número entero positivo (-1 para acabar): "))



#Ejercicio 14: Número primo

# def es_primo (numero):
#     if numero <=1:
#         return False
#     for i in range(2, numero):
#         if numero%i == 0:
#             return False
#     return True
# num_usuario = int (input("Dime un número entero positivo:"))
# if es_primo(num_usuario):
#     print(f"El número {num_usuario} es primo")
# else:
#     print(f"El número {num_usuario} no es primo")


#Ejercicio 15: Banca online

# saldo= 0
# opcion = -1
#
# while opcion != 4:
#     print("Escoge una opción: ")
#     print("1.Ingresar dinero: ")
#     print("2.Retirar dinero: ")
#     print("3.Consultar saldo: ")
#     print("4.Salir: ")
#
#     opcion = int(input())
#     if opcion == 1:
#         saldo+= int(input("¿Que cantidad deseas ingresar?: "))
#     elif opcion == 2:
#         saldo-= int(input("¿Que cantidad deseas retirar?: "))
#     elif opcion == 3:
#         print(f"Tu saldo es: {saldo} ")
#
# print("Usted ha salido del sistema")

#Ejercicio 16: Números perfectos

# numero = int (input("Dime un número entero positivo:"))
# sum_divisores = 0
#
# for i in range (1, numero):
#     if numero%i==0:
#         sum_divisores = sum_divisores+i
#
# if sum_divisores == numero:
#     print(f"El número {numero} si es un número perfecto")
# else:
#     print(f"El número {numero} no es perfecto")


#Ejercicio 17: Conversión binaria

