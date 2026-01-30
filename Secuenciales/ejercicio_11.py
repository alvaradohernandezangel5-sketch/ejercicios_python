# Pide al usuario dos números y muestra la "distancia" entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

import math 

print("Calcular distancia")

num1 = int(input("Dime el número1: "))
num2 = int(input("Dime el número2: "))

distancia = abs(num1-num2)

print("Distancia:", abs(num1-num2))