import random 

num = random.randint(1,100)

intentos = 1 

while intentos <= 10:
	num_user = int(input('Adivina el numero:'))
	if num == num_user:
		print('Bien!, Eres locoo bro!')
		print('En', intentos, 'intentos')
		break
	elif num_user < num:
		print('Uno Mayor')
	else:
		print('Uno Menor')
	intentos += 100


if intentos > 10:
	print('Perdiste Burrito!')