calf_n = int(input("ingrese la calificacion numerica:  "))

calf_letra = None

if 9 <= calf_n <= 10:
    calf_letra = "A"
elif 8 <= calf_n < 9:
    calf_letra = "B"
elif 7 <= calf_n < 8:
    calf_letra = "C"
elif 6 <= calf_n < 7:
    calf_letra = "D"
elif 0 <= calf_n < 6:
    calf_letra = "F"
else:
    print("valor desconocido")

print(f"la calificacion es {calf_letra}")
