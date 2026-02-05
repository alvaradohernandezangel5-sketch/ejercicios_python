# Dado un número de dos cifras, diseÃ±e un algoritmo que permita obtener el 
# número invertido. 

# CalcularDecenasUnidades

print("Dime un número de dos cifras")
num = int(input())

decenas = (num/10);
unidades = num % 10;

print("Primera cifra (decenas):", decenas)
print("Segunda cifra (unidades):", unidades)
