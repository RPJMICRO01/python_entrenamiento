print("imprimir del 1 al 5")

#definir la funcion recursiva
def funcion_recursiva(numero):
    #Caso Base
    if numero == 1:
        print(numero, end=" ") # 1
    else:
        funcion_recursiva(numero - 1)
        print(numero, end=" ")

funcion_recursiva(5)
