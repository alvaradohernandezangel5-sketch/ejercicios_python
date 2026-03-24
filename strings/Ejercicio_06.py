def invertir_cadena():
    cad = input("Introduce una cadena: ")
    invertida = ""

    for i in range(len(cad) - 1, -1, -1):
        invertida += cad[i]
    print(f"La cadena invertida es: {invertida}")


invertir_cadena()