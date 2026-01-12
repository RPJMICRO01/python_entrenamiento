kilos = int(input("ingrese el peso en kilogramos del paquete:  "))
destino = input("internacional o nacional:  ")

destino_2 = destino.lower().strip() == "nacional"

if not destino_2:
    mundo = 20 * kilos
else:
    mundo = 10 * kilos

print(f"el costo de envio del paquete es {mundo} en envio {destino}")
