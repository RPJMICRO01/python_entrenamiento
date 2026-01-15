notas = []

notas_a_agregar = int(input("cuantas notas desea agregar:  "))

for indice in range(notas_a_agregar):
    nota = float(input(f"Calificacion [{indice}]:  "))
    notas.append(nota)

print(f"las calificaciones proporcionadas son: {notas}")

suma_notas = sum(notas)

promedio = suma_notas / notas_a_agregar

print(f"promedio de las notas es:   {promedio}")
