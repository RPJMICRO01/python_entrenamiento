print("-"*12 + "adivina el numero entre 1 y 10" + "-"*12)
contador = 1
numero = int(input("ingrese el numero:  "))

while numero != 5:

    if numero < 5:
        print("es muy bajo")
    else:
        print("es muy alto")

    contador += 1
    numero = int(input("ingrese el numero:  "))

print(f"la cantidad de intentos que llevas son {contador}")
