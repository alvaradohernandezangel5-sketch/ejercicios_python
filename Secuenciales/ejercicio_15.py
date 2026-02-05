# IntercambiarVariables

print("Introduce valor de la variable A:")
a = int(input())

print("Introduce valor de la variable B:")
b = int(input())

aux = a;
a = b;
b = aux;

print("Nuevo valor de A:", a)
print("Nuevo valor de B:", b)