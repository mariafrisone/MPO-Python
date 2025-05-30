#Longitud de una cadena
import random

nombre = "Maria Marta Frisone"
print("Longitud del nombre: ", len (nombre))

#Convertir texto a mayusculas y minusculas
#Upper
print ("Esto soy yo en mayúsculas: ", nombre.upper())
#Lower
print("Esto soy yo en minúscula: ", nombre.lower())

#Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("últimos 4 caracteres: ", nombre[-4:])

#Reemplazar palabras en una cadena
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java", "Python"))

#Verificar su una cadena existe en otra
print("Python" in frase)
nueva_frase = "Me gusta Python"
print("Cambio a Python", nueva_frase.lower())
print("python" in nueva_frase)


#Unir varias palabras en una cadena
palabras = ["Hola", "mundo", "en", "Python"]
print("Frase completa con join: ", " " .join(palabras))

#Split
oracion = "Python es divertido"
palabritas = oracion.split()
print("Lista de palabras de mi grupo: ", palabritas)

#Redondear un número decimal
numero = 3.1416
print("Mi número redondeado es: ", round(numero))

#Formateo de números decimales
precio = 19.99
print("Precio con dos decimales: {:.2f}".format(precio) )

#Obtener el valor ASCII de un caracter
print("Esto es el código ASCII de 'A': ", ord('A'))

#Elevar al cuadrado
numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado **2)

#Como hacer la raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25 **0.5)
import math
numerito = 100
raiz = math.sqrt(numerito)
print("Raiz cuadrada de 100: ", raiz)

#Divisiones enteras y resto
print("Division normal: ",10/3)
print("Division entera: ",10//3)
print("Resto: ",10%3)

#Generar un número aleatorio
print("Número aleatorio entre 1 y 10: ", random.randint(1, 10))

#Convertir números a cadenas y viceversa
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)

cadena = "200"
numerajo = int(cadena)
print("Convertido a número soy: ", numerajo)

#Redondear hacia arriba y hacia abajo
print("Redondeo hacia arriba del número 3.6: ", math.ceil(3.6))
print("Redondeo hacia arriba del número 3.2: ", math.floor(3.2))

#Convertir una lista en un conjunto, es decir, eliminar duplicados
numeroides = [1,2,3,3,4,5,5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", sin_duplicados)

#Repetir una cadena
print("Money!" * 3)

#Tipo de dato
dato = 3.14
print("El tipo de variable de DATO es: ", type(dato))

#Combinar cadenas y variables en un print
name = "Maria"
edad = 39
print(f"Hola, soy {name} y tengo {edad} años.")