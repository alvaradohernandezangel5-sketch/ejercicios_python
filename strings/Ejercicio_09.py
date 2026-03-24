# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado.

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

indicador = False
len_cad = len(cad)
len_subcad = len(subcad)

if len_subcad <= len_cad:
    num_subcadenas = len_cad - len_subcad + 1
    for nsubc in range(num_subcadenas):
        if cad[nsubc : nsubc + len_subcad] == subcad:
            indicador = True

if indicador:
    print("La cadena contiene la subcadena ")
else:
    print("La cadena no contiene la subcadena ")
    