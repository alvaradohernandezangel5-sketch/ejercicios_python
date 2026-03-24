# Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a 
# minúsculas y viceversa.

cad = input("Introduce una cadena: ")
newcad = ""

for posicion in range(len(cad)):
    caracter = cad[posicion]
    if caracter.isupper():
        newcad += caracter.lower()
    elif caracter.islower():
        newcad += caracter.upper()
    else:
        newcad += caracter

print("La cadena convertida es:", newcad)
