NO_PRODUCTOS = 10
productos_comprados = int(input("ingrese la cantidad de productos comprados:  "))
membresia = input("tiene la membresia de la tienda (si o no) :  ")

es_elegible_descuento = productos_comprados >= NO_PRODUCTOS and membresia.strip().lower() == 'si'

print(f"es elegible para el descuento {es_elegible_descuento}")
