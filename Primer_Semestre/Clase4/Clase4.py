#Define cinco variables numéricas distintas (int, float, complex)
# y realiza diversas operaciones matemáticas (potenciación, división entera, módulo).
# Imprime los resultados formateados en una cadena clara y descriptiva.
from tokenize import String

from Proyectos.Clase3.Clase3 import palabras

num1, num2, num3, num4, num5 = 30, 10, 2.5, 4, 4+2j
resultado = (f"Potencia: {num1**num2}, División entera: {num1//num2}, "
             f"Módulo: {num2%num3}, Multiplicación: {num3*num4}, Complejo: "
              f"{num5}")
print(resultado)

# Ejercicio 2: Combinación de cadenas y números
# Define dos variables numéricas (int, float) y tres cadenas diferentes.
# Genera una nueva cadena combinando texto con el resultado de operaciones
# aritméticas entre estas variables. Usa conversión explícita
# (str()) para insertar valores numéricos en la cadena final.

num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 ="Resultado:", "La suma es ", "y la división es "
resultado2=(cadena1+""+cadena2+""+str(num_int+num_float)+""+cadena3+""
            +str(num_int/num_float))
print(resultado2)

# Ejercicio 3: Manipulación avanzada de cadenas
# Crea una cadena larga que contenga espacios en blanco al inicio, final,
# y en medio. Realiza varias operaciones encadenadas como eliminar espacios extremos,
# convertir todo a mayúsculas y dividir la cadena en varias subcadenas usando un
# separador específico.

cadena=" Esto es una cadena larga con espacios por delante y por detrás "
nueva_cadena=cadena.strip().upper().split(" ")
print(nueva_cadena)

# Ejercicio 4: Índices y subcadenas
# Define una cadena extensa (mínimo 50 caracteres). Obtén varias subcadenas
# usando la indexación por rangos (slicing) y genera una nueva cadena combinando
# estas subcadenas en orden inverso. Imprime la nueva cadena resultante.

cadena_extensa=("Esta es una nueva cadena en donde debo colocar un "
                "mínimo de cincuenta caracteres")
subcadena=cadena_extensa[0:6] + "" + cadena_extensa[11:20] + "" + cadena_extensa[-9:]
indexacion = subcadena[::-1]
print(indexacion)

# Ejercicio 5: Formato y conversión numérica
# # Define variables numéricas (entero, flotante, complejo). Crea una cadena con
# # formato avanzado (f-strings) que muestre estos números con precisión definida
# # (dos decimales, notación científica, etc.). Evita concatenar directamente números
# # y texto.

entero, flotante, complejo = 12, 345.254, 5+3j
formato=(f"Entero: {entero}, Flotante: {flotante}, Complejo: {complejo}, "
         f"Notación científica: {flotante:.2e}")
print(formato)

# Ejercicio 6: Operaciones combinadas entre números y cadenas
# Define dos variables numéricas enteras y dos cadenas. Realiza cálculos matemáticos
# diversos y genera una cadena formateada que explique cada operación (sumas, restas,
# multiplicaciones, módulo) claramente utilizando métodos de cadenas.

num_a, num_b = 15, 258
cad_a, cad_b ="La multiplicación da: ", "y el resto es: "
resultado3 = f"{cad_a} {num_a*num_b}, {cad_b}{num_a%num_b}"
print(resultado3)

# Ejercicio 7: Cálculo del área y perímetro
# Define variables numéricas que representen dimensiones (largo, ancho, radio, altura).
# Calcula el área y perímetro de distintas figuras geométricas (rectángulo, círculo,
# triángulo rectángulo) y presenta todos los resultados claramente en una sola cadena
# formateada usando conversiones explícitas.

largo, ancho, radio, altura = 15, 20, 5, 25
figuras=(f"Area rectángulo: {15*25}, Perímetro rectángulo: {2*(15+20)}, Area círculo: {3.14*5**2},"
         f" Perímetro círculo: {2*3.14*5}, Area triángulo: {(15*20)/2}")
print(figuras)

# Ejercicio 8: Análisis de texto complejo
# Define una cadena extensa que represente un párrafo completo. Utilizando únicamente
# métodos de cadenas y funciones integradas (len, upper, split), obtén el número total
# de caracteres, palabras y el resultado de transformar el texto completamente a mayúsculas,
# presentándolo claramente en una cadena nueva.

parrafo= ("Este es un párrafo de ejemplo que será usado para probar métodos de cadenas"
          "de Python")

caracteres =len(parrafo)
palabras1 =len(parrafo.split())
mayusculas =parrafo.upper()
resultado4=(f"Total caracteres: {caracteres}, total palabras: {palabras1}, texto en "
            f"mayúsculas: {mayusculas}")
print(resultado4)

# Ejercicio 9: Fórmula cuadrática
# Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática,
# resuelve la fórmula cuadrática para obtener las raíces reales o complejas. Imprime
# claramente en una cadena formateada los coeficientes y las raíces encontradas.

a,b,c=1,-3,2
discriminante=(b**2-4*a*c)**0.5
raiz1=(-b+discriminante)/(2*a)
raiz2=(-b-discriminante)/(2*a)
resolucion=f"Coeficientes: a={a}, b={b}, c={c}. Raíces: {raiz1}, {raiz2}"
print(resolucion)

# Ejercicio 10: Manejo y transformación de datos personales
# Crea variables para representar datos personales (nombre, edad, peso, altura). Calcula
# el índice de masa corporal (IMC) sin usar bucles, y presenta un resumen detallado y
# formateado de todos estos datos personales, incluyendo el IMC con dos decimales.

nombre, edad, peso, altura1= "Maria", 39, 57.5, 1.69
imc=peso/altura1**2
conclusion=(f"Nombre: {nombre}, Edad: {edad}, Peso: {peso}, Altura: {altura1},"
            f"IMC: {imc:.2f}")
print(conclusion)