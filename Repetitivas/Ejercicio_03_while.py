suma = 0 
numeros = 0
while True:
	num = int(input('Ingresa un Numero:'))
	if num == 0:
		break
	numeros += 1
	suma += num

print("La suma del numero es:" , suma)
print('El promedio de los numeros es', suma / numeros)