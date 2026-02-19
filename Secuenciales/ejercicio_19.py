print("Dime cantidad de respuestas correctas:")
correctas = int(input())

print("Dime cantidad de respuestas incorrectas:")
incorrectas = int(input())

puntos = correctas * 5 + incorrectas * (-1);

print("Puntos: ",puntos)