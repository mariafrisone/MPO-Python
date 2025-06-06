# Ejercicio 1: Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# Muestra el valor booleano de cada una.

expresion1= 10>5
expresion2= 7+3==10
expresion3= 4*2==9
expresion4= 20<15
print(expresion1, expresion2, expresion3, expresion4)

# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# Suma True + True y False + True.
# Multiplica True * 10 y False * 50.
# Muestra los resultados y explica qué ocurre

print(True+True) #True es igual a 1 y False es igual a 0
print(False+True)
print(False+False)
print(False+False)
print(False-False)
print(True*10)
print(False*50)

# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# Convierte un número en cadena y muéstralo.
# Convierte una cadena numérica en un entero.
# Convierte un booleano en un número.

numero = 850
texto=str(numero)
print("El número convertido a texto quedaría así: ", texto)



# Ejercicio 4: Propiedades de las Cadenas
# 📌 Objetivo: Manipular cadenas y explorar sus propiedades.
# Crea una cadena con tu nombre.
# Muestra el primer y último carácter.
# Muestra la longitud de la cadena.
# Convierte la cadena a mayúsculas y minúsculas.

cadena = "Maria Marta Frisone"
print("El primer caracter es:", cadena[:1], " y el último: ", cadena[-1:])
print("Longitud de la cadena: ", len(cadena))
print("Cadena en mayúsculas: ", cadena.upper(), " y cadena en minúscula: ", cadena.lower())

# Ejercicio 5: Operaciones con Cadenas y Números
# 📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
# Concatenar cadenas con números usando str().
# Multiplicar una cadena para repetirla varias veces.

edad = 39
print("Mi nombre es ", cadena,  "y tengo: ", str(edad), "años")

# Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
# 📌 Objetivo: Explorar caracteres y su representación en ASCII.
# Obtén el código ASCII de la letra 'A'.
# Convierte un número en su carácter ASCII correspondiente.

letra = "A"
print("El codigo ascii de la letra A es: ", ord(letra))
caracter = 64
print("El carácter correspondiente al numero 64 es: ", chr(caracter))

# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# Evalúa expresiones lógicas combinando números y operadores lógicos.
# Muestra los resultados.

print(10>5 and 3<8)
print(5==5 or 2>10)
print(not(4==4 and 3>1))