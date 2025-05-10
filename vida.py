print("EDixon Eliasaf Elias Villafañe")

edad = int(input("Ingresa tu edad: "))

dias = edad * 365

with open("dias.txt", "w") as archivo:
  archivo.write("Tu estimado de días vividos es " + str(edad))
