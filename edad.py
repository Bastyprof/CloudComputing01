
nombre = input("Por favor, ingresa tu nombre: ")
edad = int(input("Por favor, ingresa tu edad: "))
años_faltantes = 100 - edad
with open("edad.txt", "w") as archivo:
    archivo.write(f"Hola {nombre}, te faltan {años_faltantes} años para cumplir 100.\n")
with open("edad.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)