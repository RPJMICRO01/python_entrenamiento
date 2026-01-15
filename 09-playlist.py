lista_reproduccion = []

numero_canciones = int(input("cuantas canciones deseas agregar:  "))

for indice in range(numero_canciones):
    cancion = input(f"proporciona la cancion {indice + 1}:  ")
    lista_reproduccion.append(cancion)





# agregar estas canciones
#lista_reproduccion.append('Hotel California - Eagless')
#lista_reproduccion.append('Staying Alive - Bee Gees')
#lista_reproduccion.append('Dream on - Aerosmith')



# ordena alfabeticamente en orden asendente
lista_reproduccion.sort()
# ordena alfabeticamente en orden decendente
#lista_reproduccion.sort.(reserve = True)

print(f"\n lista de reproduccion en orden alfabetico:  ")
print(lista_reproduccion)

for cancion in lista_reproduccion:
    print(f" - {cancion}")
