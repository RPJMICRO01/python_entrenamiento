numero = input("ingrese un valor entre 1 y 12:  ")
estacion = None


if numero == "1" or numero == "2" or numero == "12":
    estacion = "Invierno"
elif numero == "3" or numero == "4" or numero == "5":
    estacion = "Primavera"
elif numero == "6" or numero == "7" or numero == "8":
    estacion = "Verano"
elif numero == "9" or numero == "10" or numero == "11":
    estacion = "Otoño"
else:
    estacio = "estacion desconocida"

print(f"el numero es {numero} pertenece a la estacion {estacion}")
