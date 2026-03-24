# Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
# palíndroma es aquella que se lee igual adelante que atrás.

cad1 = input("Ingresa una cadena: ")
cad2 = ""

for posicion in range(len(cad1) - 1, -1, -1):
    cad2 += cad1[posicion]

if cad1 == cad2:
    print("Es un palindromo")
else:
    print("No es un palindromo")