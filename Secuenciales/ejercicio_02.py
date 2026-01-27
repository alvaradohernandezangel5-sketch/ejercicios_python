# Calcular el perímetro y área de un rectángulo dada su base y su altura.






print("Cálculo de area y perímetro de un Rectangulo")
base = input('ingresa la base: ')
base = int(base)

height = input('Ingresa la altura: ')
height = int(height)

area = base * height
perimeter = base + base + height + height

print("Area:", area)
print("Perímetro:", perimeter)