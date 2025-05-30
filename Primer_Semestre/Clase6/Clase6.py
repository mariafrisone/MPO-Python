# #LISTAS
#
# # mi_lista = [10,25,30,40,50]
# # print(mi_lista[0])
# # print(len(mi_lista))
# #
# # #agregar un dato al final de la lista
# #
# # mi_lista.append(60)
# # print(mi_lista)
#
# #Ejercicio
#
# lista = [1,2,3,4,5]
# print(lista)
# lista [3]= 10
# print(lista)
# lista.append(7)
# print(lista)
#
# #TUPLAS - son inmutables
#
# mi_tupla = (1,2,3,4,5)
# print(mi_tupla)
#
# #MATRICES (primero elijo la fila y luego la columna para imprimir)
#
# mi_matriz = [[1,2,3],[4,5,6],[7,8,9]]
# print(mi_matriz[1][2])

#agregar un dato en la posición que indico
mi_lista = [1,2,3]
mi_lista.insert(1,25)
print(mi_lista)

#quito el número que quiero no posición, si hay mas de uno elimina el primer dato de izq a derecha
mi_lista.remove(3)
print(mi_lista)

#elimino posición no número
mi_lista.pop(0)
print(mi_lista)

mi_lista.reverse()
mi_lista.sort()