print("-"*12 + " GENERACION TICKER DE VENTA " + "-"*12)

PRECIO_LECHE =  float(input("precio leche:  "))
PRECIO_PAN = float(input("Precio pan:  "))
PRECIO_LECHUGA = float(input("Precio lechuga:  "))
PRECIO_PLATANO = float(input("Precio platano:  "))

#calculo del subtotal sin impuesto
subtotal = PRECIO_LECHE + PRECIO_PAN + PRECIO_LECHUGA + PRECIO_PLATANO

#CALCULO DE IMPUESTO 16%

impuesto = subtotal * 1.16

print(f"""
subtotal: ${subtotal:.2f}
impuesto 16%
Costo total ${impuesto:.2f}
      """)
