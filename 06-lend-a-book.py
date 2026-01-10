credenciales = input("tienes creedenciales de estudiante (si o no):  ")
kilometros = 3
kilometros_estudiante = int(input("a cuantos kilometros a la redonda vives:  "))

presta_libro = kilometros >= kilometros_estudiante or credenciales.strip().lower() == "si"

print(f"se le pueden prestar libros {presta_libro}")
