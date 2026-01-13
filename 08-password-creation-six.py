    
salir = False

while not salir:
    password = input("ingrese su contraseña:  ")
    six = len(password)
    if six >= 6:
        print("password valido")
        salir = True
    else:
        print("password invalida")
