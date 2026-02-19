print("Dime la velocidad del coche 1 (km/h):")
velocidad1 = int(input())

print("Dime la velocidad del coche 2 (más pequeña)(km/h):")
velocidad2 = int(input())

print("Dime la distancia entre los coches (km):")
distancia = int(input())

tiempo = distancia / (velocidad1 - velocidad2);
tiempo = tiempo * 60;

print ("Lo alcanza en ",tiempo, " minutos.")