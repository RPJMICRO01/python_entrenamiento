usuario = input("ingrese el nombre:  ")
dias_estadia = int(input("ingrese el numero de dias de estadia:  "))
vista_al_mar = input("con vista al mar SI O NO:  ")

if vista_al_mar.lower().strip() == "si":
    tarifa = dias_estadia * 190.50
else:
    tarifa = dias_estadia * 150.50

print(f"\n Client: {usuario}")
print(f"Dias de estadia:  {dias_estadia}")
print(f"costo total:  ${tarifa:.2f}") #
print(f"habitacion con vista al mar {vista_al_mar}") 
