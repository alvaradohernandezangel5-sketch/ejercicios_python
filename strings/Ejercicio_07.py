cad = input("Introduce una cadena: ")

while True:
    car_buscar = input("Introduce un caracter a buscar: ")
    if len(car_buscar) == 1:
        break
    print("Error: Solo debes ingresar un caracter ")

while True:
    car_sustituir = input("Introduce un caracter para sustituir: ")
    if len(car_sustituir) == 1:
        break
    print("Error: Solo debes ingresar un caracter ")

nuevacad = ""

for posicion in range (len(cad)):
    if cad[posicion] == car_buscar:
        nuevacad += car_sustituir
    else:
        nuevacad += cad[posicion]
print("La cadena modificada es: ", nuevacad)