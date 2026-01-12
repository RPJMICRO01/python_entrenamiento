nombre = input("ingrese el nombre del usuario:  ")
pasos_al_dia = float(input("ingrese los pasos diarios al dia:  "))

META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

calorias_quemadas = pasos_al_dia * CALORIAS_POR_PASO
meta_alcanzada = "Si" if pasos_al_dia >= META_PASOS_DIARIO else "No"

print(f"se cumplio la meta diaria {meta_alcanzada} se quemaron {calorias_quemadas} calorias")
