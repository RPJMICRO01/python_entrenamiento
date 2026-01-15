#definir una lista almacena tuplas de productos
productos = [
    ('P001','camiseta', 20.000),
    ('P002','Jeans', 30.000),
    ('P003','Sudadera', 40.000)
]

precio_total = 0

print("informacion de los productos:  ")
for producto in productos:
    id,descripcion,precio = producto # unpacking
    print(f"Producto: id = {id}, descripcion = {descripcion}, precio = {precio}")
    precio_total += precio # producto[2]
print(f"precio total de los productos:  {precio_total}")
