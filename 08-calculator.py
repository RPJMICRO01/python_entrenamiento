salir = False
while not salir:
    print("""
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5. salir
        """)
    dato = int(input("ingrese su opcion:  "))
    if dato == 1:
        valor_1 = float(input("ingrese el primer valor:  "))
        valor_2 = float(input("ingrese el primer segundo valor:  "))
        resultado = valor_1 + valor_2
        print(resultado)
    elif dato == 2:
        valor_1 = float(input("ingrese el primer valor:  "))
        valor_2 = float(input("ingrese el primer segundo valor:  "))
        resultado = valor_1 - valor_2
        print(resultado)
    elif dato == 3:
        valor_1 = float(input("ingrese el primer valor:  "))
        valor_2 = float(input("ingrese el primer segundo valor:  "))
        resultado = valor_1 * valor_2
        print(resultado)
    elif dato == 4:
        valor_1 = float(input("ingrese el primer valor:  "))
        valor_2 = float(input("ingrese el primer segundo valor:  "))
        resultado = valor_1 / valor_2
        print(resultado)
    elif dato == 5:
        print("saliendo")
        salir = True
    else:
        print("valor invalido")



