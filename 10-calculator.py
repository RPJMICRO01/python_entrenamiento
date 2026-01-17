def mostrar_menu():
    print(f""" 
    1. Suma
    2. Resta
    3. Multiplicacion
    4. Division
    5. Salir""")
    return int(input("Escoger una opcion:  "))

def pedir_valores():
    operando1 = float(input("Dame el valor 1:  "))
    operando2 = float(input("Dame el valor 2:  "))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    # Solicitar los valores de los operadores
    if 1 <= opcion <= 4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1:
        resultado = operando1 + operando2
        print(f"El resultado de la suma es {resultado}\n")
    elif opcion == 2:
        resultado = operando1 - operando2
        print(f"El resultado de la resta es: {resultado}\n")
    elif opcion == 3:
        resultado = operando1 * operando2
        print(f"El resultado de la multiplicacion es {resultado}\n")
    elif opcion == 4:
        resultado = operando1 / operando2
        print(f"El resultado de la division es {resultado}\n")
    elif opcion == 5:
        print("Saliendo del programa de calculadora, hasta pronto!")
        salir = True
    else:
        print("Opcion invalida, selecciona otra opcion...\n")
    return salir

if __name__ == "__main__":
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)
