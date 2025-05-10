nombre=input("ingresa tu nombre: ")
edad=int(input("ingresa tu edad: "))
resto=100-edad

with open('resultado.txt', 'w') as file:
    file.write(resto)

print("te faltan",resto,"años para los 100.")
