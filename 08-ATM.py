print("-"*12 + "ATM" + "-"*12)

salir = False
saldo = 1000

while not salir:
    print(f"""
    1. depositar
    2. retirar
    3. consultar el saldo
    4. salir
    """)
    
    dato = int(input("\ningrese su opcion:  "))
    if dato == 1:
        ingresar = int(input("indique el monto a ingresar:  "))
        saldo = saldo + ingresar
    elif dato == 2:
        retira = int(input("indique el monto a retirar:  "))
        saldo = saldo - retira
    elif dato == 3:
        print(f"su saldo es de {saldo}")
    else:
        salir = True
        print("saliendo")

