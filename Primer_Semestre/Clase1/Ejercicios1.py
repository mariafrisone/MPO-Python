#Ejercicio 1

primer_numero = 50
segundo_numero = 140
print("La suma de estos números es: ", primer_numero+segundo_numero)

numero_flotante = 6.32514
print("Este número dividido dos es: ", numero_flotante/2)

#Ejercicio 2

valor_verdadero = 15>8
print("¿Es real el valor declarado?: ", valor_verdadero)

con_hielo= "El vino se puede tomar con hielo"
sin_hielo ="El vino también se puede tomar sin hielo"

print("¿Como se puede tomar el vino?: ", con_hielo and sin_hielo)

expresion3 ="Pedro y Juan se fueron de vacaciones juntos"
expresion4 ="Juan se fue solo"

print("¿Con quien se fue de vacaciones Juan?: ", expresion3 or expresion4)

#Ejercicio 3

mi_nombre = 'Maria Marta Frisone'
print("Mi nombre tiene:", len (mi_nombre) , "letras")
print("Hola, mi nombre es ", mi_nombre, "y actualmente curso el primer año del FP de DAM")
print("Mi nombre en minúscula: ",  mi_nombre.lower())
print("Mi nombre en mayúscula: ", mi_nombre.upper())

slicing = mi_nombre[0:3]
print("Las 3 primeras letras de mi nombre son: ", slicing)
