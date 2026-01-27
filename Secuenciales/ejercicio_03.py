 # Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
 # calcular su hipotenusa.

cateto_1 = int(input('ingresa el cateto 1:'))
cateto_2 = int(input('ingresa el cateto 2: '))

hipotenusa = (cateto_1 ** 2 + cateto_2 ** 2) ** (1 / 2)

print('la hipotenusa es:',hipotenusa)