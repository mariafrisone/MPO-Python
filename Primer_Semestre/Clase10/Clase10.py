#Datos complejos: Listas

# mi_lista=[1,2,3,4,5]
# # print(f"Elemento popeado: {mi_lista.pop()}")
# # print("Lista popeada: ", mi_lista)
#
# # mi_lista.append(6)
# # print("Lista con nuevo elemento: ", mi_lista)
#
# mi_lista.insert(6,6)
# print("Lista con nuevo elemento en posición específica: ", mi_lista)
#
# mi_lista.remove(3)
# print(mi_lista)
#
# print("Lista ordenada: ", mi_lista.sort())
#
# print("Lista invertida: ", mi_lista.reverse())
#
# print("Longitud de la lista: ", len(mi_lista))

#Ejercicio 1: Sumar elementos de una lista
#Opcion 1 con for común
# mi_lista = input("Dime una lista ordenada de números separados por coma: ").split(",")
# resultado = 0
# for i in range(len(mi_lista)):
#     resultado += int(mi_lista[i])
# print(f"Resultado: {resultado}")

#Opción 2 con for each
# mi_lista = input("Dime una lista ordenada de números separados por coma: ").split(",")
# resultado = 0
# for numero in mi_lista:
#     resultado += int(numero)
# print(f"Rsultado: {resultado}")

#Opción 3 más pro y avanzada:
# mi_lista = input("Dime una lista ordenada de números separados por coma: ").split(",")
# lista_numero = [int(num) for num in mi_lista]
# resultado = 0
# for numero in lista_numero:
#     resultado += numero
# print(f"Resultado: {resultado}")


#Ejercicio 2: Contar elementos de una lista
# mi_lista = input("Dime una lista ordenada de palabras separadas por coma: ").split(",")
# print(f"Resultado: {len(mi_lista)}")

# lista_palabras = input("Dime una lista de palabras separadas por coma: ").split(",")
# resultado = 0
# for palabras in lista_palabras:
#     resultado += 1
# print(f"Resultado: {resultado}")

#Ejercicio 3: Mayor y menor elemento de una lista

# mi_lista = input("Dime una lista ordenada de números separados por coma: ").split(",")
# mi_lista = [int (num) for num in mi_lista]
# mi_lista.sort()
# print(f"menor: {mi_lista[0]} mayor: {mi_lista[-1]}")
# print(f"menor: {min(mi_lista)} mayor: {max(mi_lista)}")

#Ejercicio 4: Sumar dos listas de igual longitud

# mi_lista = input("Dime una lista ordenada de números separados por coma: ").split(",")
# mi_lista1 = input("Dime otra lista ordenada de números separados por coma: ").split(",")
# if len(mi_lista) != len(mi_lista1):
#     print("Error")
# else:
#     #Defino una lista nueva para el resultado
#     suma_listas = []
#     #Recorro las dos listas de entrada a la vez con el mismo índice
#     for i in range(len(mi_lista)):
#         #Añadir a la última posición de la lista resultado la suma de los valores
#         #casteados a entero de esa posición de las listas entrantes
#         suma_listas.append(int(mi_lista[i]) + int(mi_lista1[i]))
#         #Imprimo la lista resultante
#     print(f"La suma de las listas es: {suma_listas}")

#Ejercicio 5: Invertir una lista

# mi_lista = input("Dime una lista ordenada de números: ").split(" ")
# mi_lista.reverse()
# print(f"El orden inverso de la lista es: {mi_lista}")

#Ejercicio 6: Días de la semana
#
# lista_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
# while True:
#     numero = int(input("Ingrese un número (0 para salir): "))
#     if numero == 0:
#         print("Programa terminado")
#         break
#     print(lista_dias[(numero%7)-1])