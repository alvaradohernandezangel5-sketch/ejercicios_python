# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada 
# y su raíz cúbica.
# PSeInt no tiene ninguna función predefinida que permita calcular la raíz cúbica,
# ¿cómo se puede calcular?

import  math

print("Calcular raices")

num = int(input("Dime el numero: "))

raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1/3)

print("Raiz cuadrada: ", raiz_cuadrada)
print("Raiz cubica: ", raiz_cubica)
