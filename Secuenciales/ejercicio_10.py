# Un alumno desea saber cual será su calificación final en la materia de Algoritmos
# Dicha calificación se compone de los siguientes porcentajes:

print("Calcular nota")

parcial11 = float(input("Dame la nota_1: "))
parcial12 = float(input("Dame la nota_2: "))
parcial13 = float(input("Dame la nota_3: "))
examen = float(input("Dame la nota del examen: "))
trabajo = float(input("Dame la nota del trabajo: "))

nota = float((parcial11 + parcial12 + parcial13)/3) * 0.55 + 0.3 * examen + 0.15 * trabajo 

print("Nota_final",nota