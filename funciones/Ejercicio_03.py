# Función calcularTemperaturaMedia: Recibe dos números reales que representan 
# dos temperaturas y devuelve la temperatura media.
# Parámetros de entrada: dos temperaturas (real)
# Dato devuelto: La temperatura media (real)

def calcular_temperatura_media(temp1, temp2):
    tmedia = (temp1 + temp2) / 2
    return tmedia 

cantidad = int(input("¿Cuantas temperaturas vas a calcular?: "))

for indice in range (1, cantidad + 1):
    tmin = float(input("Introduce temperatura minima: "))
    tmax = float(input("Introduce temperatura maxima: "))
     
    media = calcular_temperatura_media(tmin, tmax)
    print("Temperatura media:", media)