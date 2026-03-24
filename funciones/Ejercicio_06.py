# Procedimiento CalcularAreaPerimetro: recibe el radio de una circunferencia y
# devuelve el área y el perímetro.
# Parámetros de entrada: radio (real)
# Parámetros de entrada y salida: área y perímetro (real)

import math 

def calcular_area_perimetro(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

def main():
    radio = float(input("Introduce el radio: "))

    area, perimetro = calcular_area_perimetro(radio)

    print("Area: ", area)
    print("Perimetro: ", perimetro)

if __name__ == "__main__":
    main()