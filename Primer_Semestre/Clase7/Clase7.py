#Estructuras de control y repaso con Jordi

# numero=1
# print(numero)
# numero = "Jordi"
# print(numero)
# if numero == 10:
#     print("Es diez")
# elif numero != 10:
#     print("No es diez")
# else:
#     print("No es número")

#Ejercicio 1: Siempre negativo, nunca positivo

# entero = int(input("Dime un número entero "))
# if entero >= 0:
#     print("El numero es positivo")
# else:
#     print("Es negativo")

#Ejercicio 2: Portero de discoteca

#edad = int(input("Dime tu edad: "))
# if edad >=18 and edad <=60:
#     print("Puedes ingresar")
# elif edad > 60:
#     print("Vete a la discoteca de adultos")
# else:
#     print("Vete a casa")

#Ejercicio 3: PacMan

# pos_pacman = int(input("¿Cuál es la posición del pacman?: "))
# pos_fantasma = int(input("¿Cuál es la posición del fantasma?: "))
#
# #Comprobamos que la posición sea igual
# if pos_pacman == pos_fantasma:
#     estado_pacman = input("¿Cómo está pacman?: ")
#     if estado_pacman == "caramelo":
#         print("Pacman se ha comido al fantasma")
#     else:
#         print("Pacman ha sido atrapado")
# else:
#     print("Pacman ha escapado")

#Ejercicio 4: Múltiplos de 3 y de 5

# numero_entero = int(input("Dime un número entero: "))
# if numero_entero %3 == 0 and numero_entero %5 == 0:
#         print(f"{numero_entero} es múltiplo de 3 y de 5")
# elif numero_entero %3 == 0:
#     print(f" {numero_entero} es múltiplo de 3")
# elif numero_entero %5 == 0:
#     print(f"{numero_entero} es múltiplo de 5")
# else:
#     print(f"{numero_entero} no es múltiplo de 3 ni de 5")

#Ejercicio 5: ¿Puede entrar en el servidor de Discord?

rol = input("Dime un rol ").lower()
academia = input("Dime tu academia ").lower()

if rol == "alumno" and academia == "Prometeo":
    print("Puedes ingresar al servidor")
elif rol == "profesor" and academia == "Prometeo":
    print("Tienes acceso al servidor oficial")
else:
    print("No tienes acceso")