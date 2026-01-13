salir = False
while not salir:
    print(f"""
    1. Crear cuenta
    2. Eliminar cuenta
    3. Salir
    """)
    dato = int(input("\ningrese su opcion:  "))
    if dato == 1:
        print("creando cuenta")
    elif dato == 2:
        print("eliminando cuenta")
    else:
        salir = True
        print("salir")
