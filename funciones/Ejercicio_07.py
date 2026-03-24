# Función Login: Recibe un nombre de usuario y una contraseña, y devuelve un
# valor lógico: verdadero si se ha introducido el nombre y la contraseña adecuadas.
# Además va incrementa el numero de internos que la recibe como parámetro de 
# entrada/salida
# Parámetros de entrada: nombre y contraseña
# Parámetros de entrada y salida: intentos
# Dato devuelto: Valor lógico indicando si ha hecho login

def login(nombre, contrasena, intentos):
    es_login_correcto = False
    if nombre == "Usuario1" and contrasena == "asdasd":
        es_login_correcto = True
    else:

        intentos[0] += 1
    return es_login_correcto


if __name__ == "__main__":
    intentos_fallidos = [0]
    MAX_INTENTOS = 3

    while intentos_fallidos[0] < MAX_INTENTOS:
        usuario = input("Ingresa el nombre de usuario: ")
        clave = input("Introduce la contraseña: ")
        login_exitoso = login(usuario, clave, intentos_fallidos)
        if login_exitoso:
            print("¡Login exitoso! Bienvenido al sistema.")
            break
        else:
            intentos_restantes = MAX_INTENTOS - intentos_fallidos[0]
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")

    if intentos_fallidos[0] >= MAX_INTENTOS:
        print("Se han agotado todos los intentos. Acesso degenado")
