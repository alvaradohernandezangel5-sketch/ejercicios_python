def calcular_factorial(num):
    if num == 1:
        return 1
    else: 
        return num * calcular_factorial(num - 1)
    
if __name__ == "__main__":
    numero1 = int(input("Numero: "))
    if numero1 < 1:
        print("El factorial solo se calcula para numeros enteros positivos.")
    else:
        resultado = calcular_factorial(numero1)
        print(f"El factorial es: {resultado}")