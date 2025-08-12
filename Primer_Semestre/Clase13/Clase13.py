#MODULOS
import os

def listar_archivos(ruta):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre,"x")

def crear_directorio(nombre):
    try:
        os.mkdir()
    except FileExistsError:
        raise FileExistsError

    return nombre

def obtener_extension(archivo):
    if os.path.isdir(archivo):
        return "dir"
    elif os.path.isfile()

def main():
    opcion = -1
    while opcion != 5:
        print("### MENU ###")
        print("1. Listar archivos")
        print("2. Verificar existencia archivo")
        print("3. Crear archivo")
        print("4. Crear directorio")
        print("5. Salir")

        opcion = int(input("Escoge una opción:\n"))

        if opcion == 1:
            ruta = input("Introduce la ruta que quieres consultar:\n")
            try:
                archivos = listar_archivos(ruta)
                for archivo in archivos:
                    print(archivo)
            except:
                print(f"La ruta {ruta} no existe")

        elif opcion == 2:
            archivo = input("¿Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("Archivo existe")
            else:
                print("No existe archivo")
        elif opcion == 3:
            nombre = input("¿Qué nombre quieres ponerle al archivo?\n")
            if existe_archivo(nombre):
                print("Este archivo ya existe")
            else:
                archivo = crear_archivo(nombre)
                print(f"Archivo {archivo.name} creado con éxito")
        elif opcion == 4:
            nombre = input("¿Qué nombre le quieres poner al directorio?\n")
            try:
                crear_directorio(nombre)
                print(f"Directorio {nombre} creado con éxito")
            except FileExistsError:
                    print("Este directorio ya existe")

        elif opcion > 5:
            print("Opción no válida")