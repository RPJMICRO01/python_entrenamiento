print("-"*12 + "VALOR POSITIVO" + "-"*12)

numero = int(input("PROPORCIONA UN NUMERO:  "))

if numero > 0:
    print(f"el numero es {numero} positivo")
elif numero == 0:
    print("el numero es 0")
else:
    print(f"el numero es negativo {numero}")
