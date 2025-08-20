def lista_preguntas():
    preguntas = [
        {
        "pregunta": "1. ¿Cuál es el planeta más grande del sistema solar?\n",
        "opciones": ["a) Marte\n", "b) Júpiter\n", "c) Saturno\n", "d) Tierra\n"],
        "correcta": "b"
        },
        {
        "pregunta": "2. ¿Cuál es el océano más grande del mundo?\n",
        "opciones": ["a) Océano Atlántico\n", "b) Océano Índico\n", "c) Océano Ártico\n", "d) Océano Pacífico\n"],
        "correcta": "d"
        },
        {
        "pregunta": "3. ¿Cuál es el animal terrestre más rápido?\n",
        "opciones": ["a) León\n", "b) Tigre\n", "c) Guepardo\n", "d) Antílope\n"],
        "correcta": "c"
        },
        {
        "pregunta": "4. ¿Cuál es el deporte más popular de España?\n",
        "opciones": ["a) Baloncesto\n", "b) Tenis\n", "c) Fútbol\n", "d) Ciclismo\n"],
        "correcta": "c"
        },
        {
        "pregunta": "5. ¿Cuál es el libro más vendido de todos los tiempos?\n",
        "opciones": ["a) Don Quijote de la Mancha\n", "b) Cien años de soledad\n", "c) La Biblia\n", "d) Harry Potter y la piedra filosofal\n"],
        "correcta": "c"
        }
    ]
    return preguntas

def mostrar_preguntas(pregunta):
    print(f"\n{pregunta['pregunta']}")
    for opcion in pregunta["opciones"]:
        print(opcion)

def obtener_respuestas():
    while True:
        respuesta = input("¿Cuál es la respuesta correcta?:").lower()
        if respuesta in ["a", "b", "c", "d"]:
            return respuesta
        else:
            print("Respuesta inválida. Ingresa a, b, c o d")

def corregir_respuesta(respuesta_usuario, respuesta_correcta):
    return respuesta_usuario == respuesta_correcta

def mostrar_resultados(puntuacion):
    total_preguntas = 5
    porcentaje = (puntuacion/(total_preguntas*10))*100

    print("\n" + "="*40)
    print("¡Has completado el cuestionario!")
    print(f"Tu puntuación total es: {puntuacion} de {total_preguntas * 10} puntos.")
    print(f"Tu porcentaje de aciertos es: {porcentaje:.2f}%")

    if puntuacion == 50:
        print("¡Eres muy buen@ respondiendo!")
    elif puntuacion >=20 and puntuacion <=40:
        print("¡Casi lo logras!")
    else:
        print("¡Debes practicar más!")
    print("="*40 + "\n")

opcion = 0
puntuacion = 0

while opcion !=3:
    print("* Test de preguntas *")
    print("1. Empezar cuestionario")
    print("2. Ranking")
    print("3. Salir")
    opcion = int(input("Escoge una opción:\n "))

    if opcion == 1:
        preguntas = lista_preguntas()
        puntuacion = 0
        for pregunta in preguntas:
            mostrar_preguntas(pregunta)
            respuesta_usuario = obtener_respuestas()
            if corregir_respuesta(respuesta_usuario, pregunta["correcta"]):
                print("¡Correcto! Sumas 10 puntos")
                puntuacion += 10
            else:
                print(f"Respuesta incorrecta. La respuesta correcta es: {pregunta ['correcta']}")
        mostrar_resultados(puntuacion)

    elif opcion == 2:
        print("\n" + "-"*40)
        print("Ranking de puestos")
        if puntuacion == 50:
            print("Tienes el primer puesto🥇\n")
        elif puntuacion == 40:
            print("Tienes el segundo puesto🥈\n")
        elif puntuacion == 30:
            print("Tienes el tercer puesto🥉\n")
        else:
            print(f"Tu puntuación es de {puntuacion} puntos. No has alcanzado a estar en el top 3.")
        print("-"*40 + "\n")

    elif opcion == 3:
        print("Saliendo del menú...")

    else:
        print("Opción no válida. Debes escoger 1, 2 o 3 ")


