suscriptores = set()
print(f"lista de suscriptores iniciales {suscriptores}")

numero_suscriptores = int(input(f"proporciona el numero de suscriptores iniciales:  "))
for _ in range(numero_suscriptores):
    suscriptores.add(input("nuevo suscriptor (email): "))

print(f"lista de suscriptores iniciales: {suscriptores}")


#verifica si un nueva suscriptor ya esta en la lista
nuevo_suscriptor = input("proporciona el nuevo suscriptor:   ")
if nuevo_suscriptor in suscriptores:
    print(f"el nuevo suscriptor ya esta en la lista {nuevo_suscriptor}")
else:
    suscriptores.add(nuevo_suscriptor)
    print(f"El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}")
print(f"lista de suscriptores:  {suscriptores}")

# eliminar un suscriptor
suscriptor_eliminar = input("proporciona el suscriptor a eliminar: ")
suscriptores.remove(suscriptor_eliminar)
print(f"el suscriptor {suscriptor_eliminar} ha sido eliminado de la lista")
print(f"lista de suscriptores: {suscriptores}")

# verificamos la cantidad total de suscriptores
print(f"cantidad total suscriptores: {len(suscriptores)}")

#mostramos todos los suscriptores
print(f"--- lista de suscriptores ---")
for suscriptor in suscriptores:
    print(f"- {suscriptor}")

