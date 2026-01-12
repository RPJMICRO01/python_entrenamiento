monto_compra = float(input("CUAL fue el monto de la compra:  "))
miembro = input("ERES EL MIEMBRO DE LA TIENDA (si O no):  ")

if 1000 <= monto_compra and miembro.lower().strip() == "si":
    print("Felicidades, has obtenido un descuento del 10%")
    print(f"el monto de la compra:  ${monto_compra:.2f}")
    descuento = monto_compra * 0.10
    print(f"el descuento es de {descuento}")
    monto_total= monto_compra - descuento
    print(f"Monto final de la compra con descuento {monto_total}")

elif 1000 < monto_compra or miembro.lower().strip() == "si":
    print("Felicidades, has obtenido un descuento del 5%")
    print(f"el monto de la compra:  ${monto_compra:.2f}")
    descuento = monto_compra * 0.05
    print(f"el descuento es de {descuento}")
    monto_total = monto_compra - descuento
    print(f"Monto final de la compra con descuento {monto_total}")
else:
    print(f"tu monto total es {monto_compra}")
