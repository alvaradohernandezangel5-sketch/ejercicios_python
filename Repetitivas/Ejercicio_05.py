while True:

	while True:
		car = input('Introduce un caracter: ')
		if len(car) == 1:
			break
		else:
			print("Por favor, introduce solo un caracter ")


	if car == " ":
		break

	if car.upper() in ["A", "E", "I", "O", "U"]:
		print("Vocal")
	else:
		print("No vocal")

salir = input("Quieres salir? ")
