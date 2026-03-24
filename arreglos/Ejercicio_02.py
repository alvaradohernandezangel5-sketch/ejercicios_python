def VectorInverso():
    Vector1 = [""] * 5
    Vector2 = [""] * 5
    indicador1, indicador2 = 0, 0
    tam_vector1, tam_vector2 = 0, 0
    tam_vector1 = 5
    tam_vector2 = 5
    for indicador1 in range (0, tam_vector1):
        print(f"Damela cadena {indicador1+1}:", end="")
        Vector1[indicador1] = input()
    indicador2 = 0
    for indicador1 in range(tam_vector1 -1, -1, -1):
        Vector2[indicador2] = Vector1[indicador1]
        indicador2 = indicador2 + 1
    for indicador2 in range(0, tam_vector2):
        print(f"La cadena {indicador2+1}: \"{Vector2[indicador2]}\"")
VectorInverso()