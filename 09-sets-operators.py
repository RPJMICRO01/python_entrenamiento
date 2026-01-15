a = {1,2,3,4}
b = {3,4,5,6}

# para la union usar este simbolo |
union = a | b
print(f"Union a | b: {union}")

# muestra los valores que coinciden en ambos conjuntos
interseccion = a & b
print(f"Iterseccion a & b {interseccion}")

# muestra los elementos que estan en a y no en b 
diferencia = a-b
print(f"Diferencia a - b {diferencia}")
