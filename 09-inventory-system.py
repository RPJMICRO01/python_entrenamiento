inventario = []

numero_productos = int(input("Cuantos productos deseas agregar al inventario:  "))

for indice in range(numero_productos):
    print(f"Proporciona los valores del producto {indice +1 }")
    nombre = input("Nombre:  ")
    precio = float(input("Precio:  "))
    cantidad = int(input("Cantidad:  "))
    # Creamos el diccionario con el detalle del producto
    producto = {"id": indice, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    # agregamos el nuevo producto al inventario
    inventario.append(producto)

# mostrar el inventario inicial
print(f"\n inventario inicial: {inventario}")

# Buscar un producto por id
id_buscar = int(input("\nIngresa el ID del producto a buscar:  "))
producto_encontrado = None
for producto in inventario:
    if producto.get("id") == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print("Informacion de producto encontrado")
    print(f"""Id: {producto_encontrado.get("id")}
    Nombre: {producto_encontrado.get("nombre")}
    Precio: {producto_encontrado.get("precio")}
    Cantidad: {producto_encontrado.get("cantidad")}""")
else:
    print(f"Producto con id {id_buscar} No encontrado")

print(f"\n--- Inventario Detallado ---")
for producto in inventario:
    print(f"""Id: {producto.get("id")}
    Nombre: {producto.get("nombre")}
    Precio: {producto.get("precio")}
    Cantidad: {producto.get("cantidad")}
""")
