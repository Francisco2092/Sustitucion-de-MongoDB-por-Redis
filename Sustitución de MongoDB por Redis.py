import redis

cliente = redis.Redis(host="servidor", port=puerto, password="contraseña")

def agregar_palabra():
    palabra = input("Ingresa la palabra: ")
    significado = input("Ingresa el significado: ")
    cliente.set(palabra, significado)

def editar_palabra():
    palabra = input("Ingresa la palabra que deseas editar: ")
    nuevo_significado = input("Ingresa el nuevo significado: ")
    if cliente.exists(palabra):
        cliente.set(palabra, nuevo_significado)
    else:
        print("La palabra no fue encontrada en el diccionario.")

def eliminar_palabra():
    palabra = input("Ingresa la palabra que deseas eliminar: ")
    if cliente.exists(palabra):
        cliente.delete(palabra)
    else:
        print("La palabra no fue encontrada en el diccionario.")

def ver_palabras():
    palabras = cliente.keys("*")
    for palabra in palabras:
        significado = cliente.get(palabra)
        print(f"{palabra.decode()}: {significado.decode()}")

def buscar_palabra():
    palabra = input("Ingresa la palabra que deseas buscar: ")
    significado = cliente.get(palabra)
    if significado:
        print(significado.decode())
    else:
        print("La palabra no fue encontrada en el diccionario.")

def menu():
    while True:
        print("Seleccione una opción:")
        print("a) Agregar nueva palabra")
        print("b) Editar palabra existente")
        print("c) Eliminar palabra existente")
        print("d) Ver listado de palabras")
        print("e) Buscar significado de palabra")
        print("f) Salir")

        opcion = input("Opción seleccionada: ")

        if opcion == "a":
            agregar_palabra()
        elif opcion == "b":
            editar_palabra()
        elif opcion == "c":
            eliminar_palabra()
        elif opcion == "d":
            ver_palabras()
        elif opcion == "e":
            buscar_palabra()
        elif opcion == "f":
            break
        else:
            print("Opción no válida.")
