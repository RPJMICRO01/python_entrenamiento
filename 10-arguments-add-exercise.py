def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total



# llamamos a la funcion sumar
resultado = sumar(1,2,3,4,5) # se suman los numeros del 1 al 5
print(f"Resultado de la suma {resultado}")


