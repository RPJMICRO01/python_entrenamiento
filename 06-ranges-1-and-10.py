#esta dentro del rango 1 y 10
dato = int(input("Proporcionaa un dato entero:  "))


rango_dentro_Dee = 1 <= dato <= 10
print(f"esta dentro del rango {rango_dentro_Dee}")
#esta fuera del rango 1 y 10

rango_2 = not rango_dentro_Dee 

print(f"esta fuera de rango {rango_2}")
