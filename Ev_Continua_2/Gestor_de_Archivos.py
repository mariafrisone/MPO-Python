import os
import time
from datetime import datetime

def mostrar_menu():
    print("Escoge una opcion:")
    print("1- Listar contenido del directorio actual")
    print("2- Crear nuevo directorio")
    print("3- Crear un archivo de texto")
    print("4- Escribir texto en un archivo existente")
    print("5- Eliminar un archivo o directorio")
    print("6- Mostrar información del archivo")
    print("7- Salir")
    try:
        opcion = input("Selecciona una opción (1-7): \n")
        return opcion
    except Exception as e:
        print(e)

def mostrar_ruta_actual():
    print(f"\n[Ruta Actual]: {os.getcwd()}")

def listar_contenido():
    elementos = os.listdir(os.getcwd())
    if not elementos:
        print("\nEl directorio actual está vacío")
        return

    print("\nContenido del directorio actual:")
    for elemento in elementos:
        ruta_completa = os.path.join(os.getcwd(), elemento)
        if os.path.isdir(ruta_completa):
            tipo = "[DIR]"
        elif os.path.isfile(ruta_completa):
            tipo = "[FILE]"
        else:
            tipo = "[OTRO]"
        print(f"{tipo} {elemento}")


def crear_directorio():
    nombre_dir = input("Ingresa el nombre para el nuevo directorio: \n").strip()
    if not nombre_dir:
        print("Error. El nombre del directorio no puede estar vacío")
        return
    try:
        os.mkdir(nombre_dir)
        print(f"Directorio {nombre_dir} ha sido creado con éxito")
    except FileExistsError:
        print(f"Ya existe un archivo o directorio con ese nombre {nombre_dir}")
    except ValueError as e:
        print(f"No se pudo crear el directorio {nombre_dir} {e}")

def crear_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo de texto que quiere crear:\n")
    if not nombre_archivo:
        print("El nombre del archivo no puede estar vacío")
        return
    if os.path.exists(nombre_archivo):
        print(f"Ya existe un archivo con ese nombre {nombre_archivo}")
        return
    try:
        contenido = input("Ingrese el contenido inicial para el archivo")
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido + "\n")
        print(f"Archivo {nombre_archivo} creado con éxito")
    except ValueError as e:
        print(e)

def escribir_en_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo que desea escribir:\n").strip()
    if not os.path.exists(nombre_archivo):
        print(f"El archivo {nombre_archivo} no existe")
        return
    if not os.path.isfile(nombre_archivo):
        print(f"{nombre_archivo} no es un archivo de texto")
        return
    try:
        nuevo_contenido = input("Ingresa el texto que quieres añadir:\n")
        with open(nombre_archivo, 'a') as f:
            f.write("\n" + nuevo_contenido)
        print(f"Contenido añadido")
    except ValueError as e:
        print(e)

def eliminar_elemento():
    nombre_elemento = input("Ingresa el nombre del archivo o directorio que quieres eliminar:\n")
    if not nombre_elemento:
        print("El nombre no puede estar vacío")
        return

    try:
        ruta_completa = os.path.join(os.getcwd(), nombre_elemento)
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)
            print(f"El archivo {nombre_elemento} se ha eliminado correctamente")
        elif os.path.isdir(ruta_completa):
            os.rmdir(ruta_completa)
            print(f"El directorio {nombre_elemento} se ha eliminado correctamente")
        else:
            print(f"{nombre_elemento} no es un archivo ni un directorio")
    except ValueError as e:
        print(e)

def mostrar_informacion():
    nombre_elemento = input("Ingresa el nombre del archivo o directorio que quieres ver\n")
    if not nombre_elemento:
        print("El nombre no puede estar vacío")
        return
    try:
        ruta_completa = os.path.join(os.getcwd(), nombre_elemento)
        if not os.path.exists(ruta_completa):
            print(f"El elemento {nombre_elemento} no existe en la ruta actual")
            return
        info = os.stat(ruta_completa)
        if os.path.isdir(ruta_completa):
            tipo = "Directorio (Carpeta)"
        elif os.path.isfile(ruta_completa):
            tipo = "Archivo de texto"
        else:
            tipo = "Otro tipo de elemento"

        size = info.st_size
        if size < 1024:
            size_fmt = f"{size} bytes"
        elif size < 1024 * 1024:
            size_fmt = f"{size/1024:.2f} KB"
        else:
            size_fmt = f"{size/(1024 *1024):.2f} MB"

        mtime_timestamp = info.st_mtime
        fecha_modificacion = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime_timestamp))

        print(f"Información de: {nombre_elemento}")
        print(f"Tipo: {tipo}")
        print(f"Tamaño: {size_fmt}")
        print(f"Ruta Absoluta: {ruta_completa}")
        print(f"Última modificación: {fecha_modificacion}")

    except ValueError as e:
        print(e)

def main():

    while True:
        mostrar_ruta_actual()
        opcion = mostrar_menu()

        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            crear_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == "4":
            escribir_en_archivo()
        elif opcion == "5":
            eliminar_elemento()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "7":
            print("Está saliendo del gestor de archivos")
            break
        else:
            print("\nOpción no válida. Por favor ingrese un número correcto")

main()
