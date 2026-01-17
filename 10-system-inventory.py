
#inventario del almacen
inventario = [
    {"id":1, "nombre":"camisa", "precio":25.99 , "cantidad":50},
    {"id":2, "nombre":"pantalones", "precio":39.99, "cantidad":30},
    {"id":3, "nombre":"zapatos", "precio":49.99, "cantidad":50},
]

# Funcion para mostrar el inventario
def mostrar_inventario():
    print("--- Inventario del almacen ---")
    for producto in inventario:
        print(f"Id: {producto.get('id')}, Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, Cantidad: {producto.get('cantidad')}")

def agregar_producto():
    print("--- Agregar Nuevo Producto ---")
    id = int(input("Id: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    nuevo_producto = {"id": id, "nombre":nombre,
                      "precio":precio, "cantidad": cantidad}
    inventario.append(nuevo_producto)
    print("Producto agregado al inventario")


def buscar_producto_por_id():
    print("--- Buscar Producto por Id ---")
    id_buscar = int(input("Ingresa el id a buscar: "))
    for producto in inventario:
        if producto.get("id") == id_buscar:
            print("\nInformacion del producto encontrado: ")
            print(f"Id: {producto.get('id')}\n",
                  f"Nombre: {producto.get('nombre')}\n",
                  f"Precio: ${producto.get('precio')}\n",
                  f"Cantidad: {producto.get('cantidad')}")
            return
    print("\nProducto NO encontrado")


if __name__ == "__main__":
    while True:
        print(f"""\n --- Menu ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por id
        4. Salir """)
        opcion = int(input("proporciona (1-4):  "))

        # revisamos las opciones del menu
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            agregar_producto()
        elif opcion == 3:
            buscar_producto_por_id()
        elif opcion == 4:
            print("Hasta luego")
            break
        else:
            print("opcion invalida, proporciona una opcion valida")
