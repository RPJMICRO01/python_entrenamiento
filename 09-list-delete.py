mi_lista = [1,10,15,3,4,5,6]

mi_lista.remove(5)
print(f"{mi_lista} -> se removio el valor 5")

mi_lista.pop(1)
print(f"{mi_lista}")

del mi_lista[2]
print(f"{mi_lista} -> se elimino el indicee 2")

sublista = mi_lista[1:3] 
print(f"sublista [1:3]: {sublista}")
