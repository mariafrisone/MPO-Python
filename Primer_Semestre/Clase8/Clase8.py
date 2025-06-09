#Bucle for in range
#empieza por cero, llega hasta el cinco (no incluido) y ve de uno en uno
#puedo tb ir al reves (10, 0, -1)

# for i in range (0,5,1):
#     print(i)
#
# #Break y continue
#
# for i in range (11):
#     if i%2 == 1:
#         continue
#     print(i)

#Ejercicio 1: Contador

# numero = int(input("Dime un número entero positivo: "))
# for i in range(0, (numero + 1)):
#     print(i)

#Ejercicio 2: Contador de números pares

# #Recibo número de usuario
# numero = int(input("Dime un número entero positivo: "))
# #Inicializo una variable para ir contando los pares que hay en esa secuencia de números
# pares = 0
# #Para i en la secuencia [0.1.2.3.4....numero+1]
# for i in range(0, (numero+1)):
#     #Miro si i es par
#     if i %2 == 0:
#         #Si es par sumo 1 al contador de pares
#         pares = pares+1
# print(f"Número de pares {pares}")

#Ejercicio 3: Cuenta atrás

# numero = int(input("Dime un número entero positivo: "))
# for i in range(numero, 0, -1):
#     print(i)

#Ejercicio 4: Factorial

# numero = int(input("Dime un número entero positivo: "))
# factorial = 1
# for i in range(1, numero+1):
#     factorial *= i
# print(f"El factorial de {numero} es {factorial}")

#Ejercicio 5: Múltiplo de 3 o de 5

# numero = int(input("Dime un número entero positivo: "))
#
# for i in range(numero+1):
#     if i %3 == 0 and i%5 == 0:
#        continue
#     elif i %3 == 0:
#         print(f"El número {i} es múltiplo de 3")
#     elif i %5 == 0:
#         print(f"El número {i} es múltiplo de 5")

#Ejercicio 6: Triángulo de asteriscos

# numero = int(input("Dime un número entero positivo: "))
# for i in range(0, numero+1):
#     print(f"*"*i)

#Ejercicio 7: Tabla de multiplicar
#
# numero = int(input("Dime un número entero positivo: "))
#
# for i in range(1, 11):
#     print(f"{numero}*{i} = {numero*i}")

#Ejercicio 8: Cuadrado con cruz

# numero = int(input("Dime un número entero positivo impar: "))
# for i in range(numero):
#     for j in range(numero):
#         if i == 0 or i == numero - 1 or j == 0 or j == numero - 1 or i == j or i + j == numero - 1:
#             print("x", end="")
#         else:
#             print(" ", end="")
#     print()

