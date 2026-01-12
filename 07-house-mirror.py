edad = int(input("ingrese su edad:  "))
miedo = input("tienes miedo a la oscuridad SI o NO:  ")

miedo_2 = miedo.lower().strip() == "si"

if not miedo_2 and edad > 10:
    print("puedes entrar a la casa")
else:
    print("no puedes entrar a la casa")
